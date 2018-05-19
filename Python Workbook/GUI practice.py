# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:51:36 2017

@author: Data1
"""


########### open and close ############
from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
root.destroy()



########### open file ###############
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

interface = Tk()

def openfile():
    return filedialog.askopenfilename()

button = ttk.Button(interface, text="Open", command=openfile)  # <------
button.grid(column=1, row=1)

interface.mainloop()

from tkinter import *

master = Tk()

def callback():
    print ("click!")

b = Button(master, text="OK", command=callback)
b.pack()

master.mainloop()
