from tkinter import *

class PhilDialog():
    def __init__(self):
        self.parent = Toplevel()
        self.parent.geometry('250x100')
        self.parent.title('Name Dialog')
        
        self.name = StringVar()
        
        label = Label(self.parent, text="Name: ")
        label.grid(row=0, column=0)
        Entry(self.parent, textvariable=self.name).grid(row=0, column=1)
        Button(self.parent, text='OK', command=self.on_OK).grid(row=1)

    def showModal(self):
        self.parent.deiconify()     # make sure this window isn't minimised
        self.parent.grab_set()      # make this window modal
        self.parent.wait_window()   # start an event loop for this window
                                    # this function will not coninue until
                                    # this window has been destroyed (in on_OK)
        #value = self.name.get()
        return self.name.get()     

    def on_OK(self):
        name = self.name.get()
        print("Now we need to lookup %s in the database" % name)
        self.parent.destroy()       # return the name to the function in the
                                    # window that called us
