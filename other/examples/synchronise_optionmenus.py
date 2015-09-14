"""
How to change the contents of an Option Menu
based on the current options of another OptionMenu

Source: http://stackoverflow.com/questions/17252096/change-optionmenu-based-on-what-is-selected-in-another-optionmenu
"""

import tkinter as tk


class App(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.dict = {'Asia': ['Japan', 'China', 'Malasia'],
                     'Europe': ['Germany', 'France', 'Switzerland']}

        self.variable_a = tk.StringVar(self)
        self.variable_b = tk.StringVar(self)
        
        self.variable_a.trace('w', self.update_options)
        
        self.optionmenu_a = tk.OptionMenu(self, self.variable_a, *self.dict.keys())
        self.optionmenu_b = tk.OptionMenu(self, self.variable_b, '')
        
        self.variable_a.set('Asia')

        self.optionmenu_a.pack()
        self.optionmenu_b.pack()

        self.pack()

    def update_options(self, *args):
        countries = self.dict[self.variable_a.get()]
        self.variable_b.set(countries[0])

        menu = self.optionmenu_b['menu']
        menu.delete(0, 'end')
        
        for country in countries:
            menu.add_command(label=country, command=lambda country=country: self.variable_b.set(country))


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.mainloop()
