from tkinter import *
from phil_dialog import *


class App():
    def __init__(self, parent):
        self.parent = parent
        self.parent.geometry('300x200')
        self.parent.title('Dialog Demo')

        self.labelText = StringVar()
        
        self.label = Label(parent, textvariable=self.labelText)
        self.label.grid(row=0)
        self.button = Button(parent, text="GetName", command=self.on_get_name)
        self.button.grid(row=1)

    def on_get_name(self):
        dialog = PhilDialog()       # create a PhilDialog
        name = dialog.showModal()   # call it's showModal() method
        self.labelText.set("Name is: %s" % name)


root = Tk()
app = App(root)
root.mainloop()
