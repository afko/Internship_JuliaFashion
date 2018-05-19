# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 11:19:15 2017

@author: Data1
"""
import csv

file_name = input("What is csv file name? ")

f = open ("C:\\Users\data1\Desktop\\trans\\" + str(file_name) , "r" )
f_csv = csv.reader(f)

f_list = []

for row in f_csv:
    if row[2] == "Order":
        f_list.append(row[10])
        
nodup_list = list(set(f_list))

nodup_list.sort()

#2017FebMonthlyTransaction.csv