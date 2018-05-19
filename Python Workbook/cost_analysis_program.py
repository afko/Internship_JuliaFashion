# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 11:31:16 2017

@author: Data1
"""

from tkinter import filedialog as fd
from tkinter import *
import csv
import os


class CostProgram:

    def __init__(self, master):
        self.master = master
        master.title("CostCalulator")
        master.minsize(width=102, height=300)
        
               
        l1 = Label(master, width= 20, height=3, text="Transaction File Load", wraplength=80).grid(row=1, column=0)
        l2 = Label(master, width= 20, height=3, text="Cost File Load").grid(row=2, column=0)
    
        self.file_name_label1 = Label(master, width= 40, height=3, text="").grid(row=1, column=1)
        self.file_name_label2 = Label(master, width= 40, height=3, text="").grid(row=2, column=1)
    
        
        open_trans_btn = Button(master, width=17, height=3, text="Transaction File Load", \
                                command = self.openTransfile).grid(row=1, column=3 ,sticky=W+E+N+S)
        open_cost_btn = Button(master, width=17, height=3, text="CostTable File Load", \
                               command = self.openCostfile).grid(row=2, column=3, sticky=E)
        
        
    def openTransfile(self):
        self.transpath = fd.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        self.file_name_label1 = Label(self.master, width= 40, height=2, \
                                            text= os.path.split(self.transpath)[1]).grid(row=1, column=1)

        try:
            f = open(self.transpath,'r')
            print("Done")
        except:
            print("No file exists")
        
        file_trans = csv.reader(f)
        
        trans_list = []
        
        for trans_row in file_trans:
            temp_list = []
            temp_list.append(trans_row[0])
            temp_list.append(trans_row[2])
            temp_list.append(trans_row[4])
            temp_list.append(trans_row[6])
            temp_list.append(trans_row[21])
            trans_list.append(temp_list)
        print("DDone")    
        return trans_list    
    
    def openCostfile(self):
        self.costpath = fd.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        self.file_name_label2 = Label(self.master, width= 40, height=2, \
                                            text= os.path.split(self.costpath)[1]).grid(row=2, column=1)

root = Tk()
costprogram = CostProgram(root)
root.mainloop()
#root.destroy()
