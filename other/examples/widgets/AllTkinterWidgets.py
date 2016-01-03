from tkinter import *


class AllTkinterWidgets:

    def __init__(self, master):
        frame = Frame(master, width=500, height=400, bd=1)
        frame.pack()

        self.mbar = Frame(frame, relief='raised', bd=2)
        self.mbar.pack(fill=X)

        # Create File menu
        self.filebutton = Menubutton(self.mbar, text='File')
        self.filebutton.pack(side=LEFT)

        self.filemenu = Menu(self.filebutton, tearoff=0)
        self.filebutton['menu'] = self.filemenu

        # Populate File menu
        self.filemenu.add('command', label='Exit', command=self.quit)

        # Create  object menu
        self.objectbutton = Menubutton(self.mbar, text='Object', )
        self.objectbutton.pack(side=LEFT)

        self.objectmenu = Menu(self.objectbutton, tearoff=0)
        self.objectbutton['menu'] = self.objectmenu

        # Populate object menu
        self.objectmenu.add('command', label='object', command=self.stub)

        # Create  edit menu
        self.editbutton = Menubutton(self.mbar, text='Edit', )
        self.editbutton.pack(side=LEFT)

        self.editmenu = Menu(self.editbutton, tearoff=0)
        self.editbutton['menu'] = self.editmenu

        # Populate edit menu
        self.editmenu.add('command', label='edit', command=self.stub)

        # Create  view menu
        self.viewbutton = Menubutton(self.mbar, text='View', )
        self.viewbutton.pack(side=LEFT)

        self.viewmenu = Menu(self.viewbutton, tearoff=0)
        self.viewbutton['menu'] = self.viewmenu

        # Populate view menu
        self.viewmenu.add('command', label='view', command=self.stub)

        # Create  tools menu
        self.toolsbutton = Menubutton(self.mbar, text='Tools', )
        self.toolsbutton.pack(side=LEFT)

        self.toolsmenu = Menu(self.toolsbutton, tearoff=0)
        self.toolsbutton['menu'] = self.toolsmenu

        # Populate tools menu
        self.toolsmenu.add('command', label='tools', command=self.stub)

        # Create  help menu
        self.helpbutton = Menubutton(self.mbar, text='Help', )
        self.helpbutton.pack(side=RIGHT)

        self.helpmenu = Menu(self.helpbutton, tearoff=0)
        self.helpbutton['menu'] = self.helpmenu

        # Populate help menu
        self.helpmenu.add('command', label='help', command=self.stub)

        iframe1 = Frame(frame, bd=2, relief=SUNKEN)
        Button(iframe1, text='Button').pack(side=LEFT, padx=5)
        Checkbutton(iframe1, text='CheckButton').pack(side=LEFT, padx=5)

        v = IntVar()
        Radiobutton(iframe1, text='Button', variable=v,
                    value=3).pack(side=RIGHT, anchor=W)
        Radiobutton(iframe1, text='Dio', variable=v,
                    value=2).pack(side=RIGHT, anchor=W)
        Radiobutton(iframe1, text='Ra', variable=v,
                    value=1).pack(side=RIGHT, anchor=W)
        iframe1.pack(expand=1, fill=X, pady=10, padx=5)

        iframe2 = Frame(frame, bd=2, relief=RIDGE)
        Label(iframe2, text='Label widget:').pack(side=LEFT, padx=5)
        t = StringVar()
        Entry(iframe2, textvariable=t, bg='white').pack(side=RIGHT, padx=5)
        t.set('Entry widget')
        iframe2.pack(expand=1, fill=X, pady=10, padx=5)

        iframe3 = Frame(frame, bd=2, relief=GROOVE)
        listbox = Listbox(iframe3, height=4)
        for line in ['Listbox Entry One', 'Entry Two', 'Entry Three', 'Entry Four']:
            listbox.insert(END, line)
        listbox.pack(fill=X, padx=5)
        iframe3.pack(expand=1, fill=X, pady=10, padx=5)

        iframe4 = Frame(frame, bd=2, relief=SUNKEN)
        text = Text(iframe4, height=10, width=65)
        fd = open('guido.txt')
        lines = fd.read()
        fd.close()
        text.insert(END, lines)
        text.pack(side=LEFT, fill=X, padx=5)
        sb = Scrollbar(iframe4, orient=VERTICAL, command=text.yview)
        sb.pack(side=RIGHT, fill=Y)
        text.configure(yscrollcommand=sb.set)
        iframe4.pack(expand=1, fill=X, pady=10, padx=5)

        iframe5 = Frame(frame, bd=2, relief=RAISED)
        Scale(iframe5, from_=0.0, to=50.0, label='Scale widget',
              orient=HORIZONTAL).pack(side=LEFT)
        c = Canvas(iframe5, bg='white', width=340, height=100)
        c.pack()
        for i in range(25):
            c.create_oval(
                5 + (4 * i), 5 + (3 * i), (5 * i) + 60, (i) + 60, fill='gray70')
        c.create_text(260, 80, text='Canvas', font=('verdana', 10, 'bold'))
        iframe5.pack(expand=1, fill=X, pady=10, padx=5)

        iframen = Frame(frame, bd=2, relief=FLAT)
        Message(iframen, text='This is a Message widget', width=300,
                relief=SUNKEN).pack(fill=X, padx=5)
        iframen.pack(expand=1, fill=X, pady=10, padx=5)

    def quit(self):
        root.destroy()

    def stub(self):
        pass

root = Tk()
root.option_add('*font', ('verdana', 10, 'bold'))
all = AllTkinterWidgets(root)
root.title('Tkinter Widgets')
root.mainloop()
