# Why your GUI app freezes?

Source: <a href="http://stupidpythonideas.blogspot.ch/2013/10/why-your-gui-app-freezes.html">http://stupidpythonideas.blogspot.ch/2013/10/why-your-gui-app-freezes.html</a>

`Posted 18th October 2013 by barnert`


Imagine a simple Tkinter app. (Everything is pretty much the same for most other GUI frameworks, and many frameworks for games and network servers, and even things like SAX parsers, but most novices first run into this with GUI apps, and Tkinter is easy to explore because it comes with Python.)

~~~python
def handle_click():
   print('Clicked!')
   
root = Tk()
Button(root, text='Click me', command=handle_click).pack()
root.mainloop()
~~~

Now imagine that, instead of just printing a message, you want it to pop up a window, wait 5 seconds, then close the window. You might try to write this:

~~~python
def handle_click():
   win = Toplevel(root, title='Hi!')
   win.transient()
   Label(win, text='Please wait...').pack()
   for i in range(5, 0, -1):
       print(i)
       time.sleep(1)
   win.destroy()
~~~

But when you click the button, the window doesn't show up. And the main window freezes up and beachballs for 5 seconds. 

This is because your event handler hasn't returned, so the main loop can't process any events. It needs to process events to display a new window, respond to messages from the OS, etc., and you're not letting it. 

There are two basic ways around this problem: callbacks, or threads. There are advantages and disadvantages of both. And then there are various ways of building thread-like functionality on top of callbacks, which let you get (part of) the best of both worlds, but I'll get to those in another post.


##Callbacks

Your event handler has to return in a fraction of a second. But what if you still have code to run? You have to reorganize your code: Do some setup, then schedule the rest of the code to run later. And that "rest of the code" is also an event handler, so it also has to return in a fraction of a second, which means often it will have to do a bit of work and again schedule the rest to run later.

Depending on what you're trying to do, you may want to run on a timer, or whenever the event loop is idle, or every time through the event loop no matter what. In this case, we want to run once/second. In Tkinter, you do this with the `after` method:

~~~python
def handle_click():
   win = Toplevel(root, title='Hi!')
   win.transient()
   Label(win, text='Please wait...').pack()
   i = 5
   def callback():
       nonlocal i, win
       print(i)
       i -= 1
       if not i:
           win.destroy()
       else:
           root.after(1000, callback)
   root.after(1000, callback)
~~~

For a different example, imagine we just have some processing that takes a few seconds because it has so much work to do. We'll do something stupid and simple:

~~~python
def handle_click():
   total = sum(range(1000000000))
   label.config(text=total)

root = Tk()
Button(root, text='Add it up', command=handle_click).pack()
label = Label(root)
label.pack()
root.mainloop()
~~~

When you click the button, the whole app will freeze up for a few seconds as Python calculates that sum. So, what we want to do is break it up into chunks:

~~~python
def handle_click():
   total = 0
   i = 0
   def callback():
       nonlocal i, total
       total += sum(range(i*1000000, (i+1)*1000000))
       i += 1
       if i == 100:
           label.config(text=total)
       else:
           root.after_idle(callback)
   root.after_idle(callback)
~~~

### Callback Hell

While callbacks definitely work, there are a lot of probems with them.

First, we've turned out control flow inside-out. Compare the simple for loop to the chain of callbacks that replaced it. And it gets much worse when you have more complicated code.

On top of that, it's very easy to get lost in a callback chain. If you forget to return from a sequential function, you'll just fall off the end of the function and return None. If you forget to schedule the next callback, the operation never finishes.

It's also hard to propagate results through a chain of callbacks, and even harder to propagate errors. Imagine that one callback needs to schedule a second which needs to schedule a third and so on--but if there's an exception anywhere on the chain, you want to jump all the way to the last callback. Think about how you'd write that (or just look at half the Javascript apps on the internet, which you can View Source for), and how easy it would be to get it wrong.

And debugging callback-based code is also no fun, because the stack traceback doesn't show you the function that scheduled you to run later, it only shows you the event loop.

There are solutions to these problems, which I'll cover in another post. But it's worth writing an app or two around explicit callbacks, and dealing with all the problems, so you can understand what's really involved in event-loop programming.

### Blocking operations

Sleeping isn't the only thing that blocks. Imagine that you wanted to read a large file off the disk, or request a URL over the internet. How would you do that with callbacks?

We had to replace our sleep with a call to after, passing it the rest of our function as a callback. Similarly, we have to replace our read or urlopen with a call to some function that kicks off the work and then calls our callback when it's done. But most GUI frameworks don't have such functions. And you don't want to try to build something like that yourself.

I/O isn't the only kind of blocking, but it's by far the most common. And there's a nice solution to blocking I/O: asynchronous I/O, using a networking framework. Whether this is as simple as a loop around select or as fancy as Twisted, the basic idea is the same as with a GUI: it's an event loop that you add handlers to.

And there's the problem: your GUI loop and your I/O loop both expect to take over the thread, but they obviously can't both d that.

The solution is to make one loop drive the other. If either framework has a way to run one iteration of the main loop manually, instead of just running forever, you can, with a bit of care, put one in charge of the other. (Even if your framework doesn't have a way to do that, it may have a way to fake it by running an event loop and immediately posting a quit event; Tkinter can handle that.)

And the work may have already been done for you. Twisted is a networking framework that can work with most popular GUI frameworks. Qt is a GUI framework with a (somewhat limited) built-in network framework. They both have pretty high learning curves compared to Tkinter, but it's probably easier to learn one of them than to try to integrate, say, Tkinter and a custom select reactor yourself.

Another option is a hybrid approach: Do your GUI stuff in the main thread, and your I/O in a second thread. Both of them can still be callback-driven, and you can localize all of the threading problems to the handful of places where the two have to interact with each other.

## Threading

With multithreading, we don't have to reorganize our code at all, we just move all of the work onto a thread:

~~~python
def handle_click():
   def callback():
       total = sum(100000000)
       print(total)
   t = threading.Thread(target=callback)
   t.start()
~~~

This kicks off the work in a background thread, which won't interfere with the main thread, and then returns immediately. And, not only is it simpler, you don't have to try to guess how finely to break up your tasks; the OS thread scheduler just magically takes care of it for you. So all is good.

Plus, this works just as well for I/O as it does for computation (better, in fact):

~~~python
def handle_click():
   def callback():
       r = urlopen('http://example.com')
       data = r.read()
       soup = BeautifulSoup(data)
       print(soup.find('p').text)
   t = threading.Thread(target=callback)
   t.start()
~~~

But what if we want it to interfere with the main thread? Then we have a problem. And with most frameworks--including Tkinter--calling any method on any GUI widget interferes with the main thread. For example, what we really wanted to do was this:

~~~python
def handle_click():
   def callback():
       total = sum(100000000)
       label.config(text=total)
   t = threading.Thread(target=callback)
   t.start()
~~~

But if we try that, it no longer works. (Or, worse, depending on your platform/version, it often works but occasionally crashes...)

So, we need some way to let the background thread work with the GUI.

### `on_main_thread`

If you had a function on_main_thread that could be called on any thread, with any function, and get it to run on the main thread as soon as possible, this would be easy to solve:

~~~python
def handle_click():
   def callback():
       total = sum(100000000)
       root.on_main_thread(lambda: label.config(text=total))
   t = threading.Thread(target=callback)
   t.start()
~~~

Many GUI frameworks do have such a function. Tkinter, unfortunately, does not.

If you want to, you can pretty easily wrap up all of your widgets with proxy objects that forward method calls through on_main_thread, like this: 

~~~python
class ThreadedMixin:
   main_thread = current_thread()
   def _forward(self, func, *args, **kwargs):
       if current_thread() != ThreadedMixin.main_thread:
           self.on_main_thread(lambda: func(*args, **kwargs))
       else:
           func(*args, **kwargs)

class ThreadSafeLabel(Label, ThreadedMixin):
   def config(self, *args, **kwargs):
       self._forward(super().config, args, kwargs)
   # And so on for the other methods
~~~

Obviously you'd want do this programmatically or dynamically instead of writing hundreds of lines of forwarding code.

### `post_event`

If you had a function post_event that could be called on any thread to post a custom event to the event queue, you could get the same effect with just a bit of extra work--just write an event handler for that custom event. For example:

~~~python
def handle_my_custom_event(event):
   label.config(text=event.message)
root.register_custom_event('<My Custom Event>')
root.bind('<My Custom Event>', handle_custom_event)

def handle_click():
   def callback():
       total = sum(100000000)
       event = Event('<My Custom Event>', data=total)
       root.post_event(event)
~~~

Most GUI frameworks that don't have on_main_thread have post_event. But Tkinter doesn't even have that.


### Polling queues

With limited frameworks like Tkinter, the only workaround is to use a Queue, and make Tkinter check the queue every so often, something like this:

~~~python
q = queue.Queue()

def on_main_thread(func):
   q.put(func)

def check_queue():
   while True:
       try:
           task = q.get(block=False)
       except Empty:
           break
       else:
           root.after_idle(task)
   root.after(100, check_queue)

root.after(100, check_queue)
~~~

While this works, it makes the computer waste effort constantly checking the queue for work to do. This isn't likely to slow things down when your program is busy--but it will make it drain your battery and prevent your computer from going to sleep even when your program has nothing to do. Programs that use a mechanism like this will probably want some way to turn check_queue on and off, so it's only wasting time when you actually have some background work going.

### `mtTkinter`

There's a wrapper around Tkinter called mtTkinter that effectively builds on_main_thread out of something like check_queue, and then builds thread-safe proxies around all of the Tkinter widgets, so you can use Tkinter as if it were completely thread-safe.

I don't know whether it's really "production-quality". I believe it hasn't been ported to Python 3 either. (2to3 might be enough, but I can't promise that.) And the LGPL licensing may be too restrictive for some projects. But for learning purposes, and maybe for building simple GUIs for your own use, it's worth looking at.


### Threading limits

Unlike callbacks, if you pile up too many threads, you start adding additional overhead, in both time and space, on top of the cost of actually doing the work.

The solution to this is to use a small pool of threads to service a queue of tasks. The easiest way to do this is with the futures module:

~~~python
executor = ThreadPoolExecutor(8)

def handle_click():
   def callback():
       total = sum(100000000)
       root.on_main_thread(lambda: label.config(text=total))
   executor.submit(callback)
~~~
        
## Shared data

The biggest problem with threads is that any shared data needs to be synchronized, or you have race conditions. The general problem, and the solutions, are covered well all over the net.

But GUI apps add an additional problem: Your main thread can't block on a synchronization object that could be held for more than a fraction of a second, or your whole GUI freezes up. So, you need to make sure you never wait on a sync object for more than a brief time (either by making sure nobody else can hold the object for too long, or by using timeouts and retries).