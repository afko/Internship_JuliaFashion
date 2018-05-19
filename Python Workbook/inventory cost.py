# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:12:41 2017

@author: Data1
"""

import csv

##### lOAD Invnetory File #####
inv = open ("C:\\Users\data1\Desktop\\daily inventory of 102417.csv" , "r")
inv_reader = csv.reader(inv)
inv_list = []
for row in inv_reader:
    inv_list.append(row)
    
##### IMPORT Annabelle Style Cost ##### 
c = open ('C:\\Users\data1\Desktop\\transcost.csv' , "r" , encoding = 'utf8')

cost_reader = csv.reader(c)
cost_list = []
for row in cost_reader:
    cost_list.append(row)

##### Find INDEX #####    
sku_index = 0
qty_index = 0
dd_index = 0

for attribute in inv_list[0]:
    if attribute == "sku":
        sku_index
        break
    else:
        sku_index = sku_index + 1
        
for attribute in inv_list[0]:
    if attribute == "quantity":
        qty_index
        break
    else:
        qty_index = qty_index + 1
        
for attribute in inv_list[0]:
    if attribute == "detailed-disposition":
        dd_index
        break
    else:
        dd_index = dd_index + 1        

##### new_list #####
new_list = []

for row in inv_list:
    temp_list = []
    temp_list.append(row[sku_index])
    temp_list.append(row[qty_index])
    temp_list.append(row[dd_index])
    new_list.append(temp_list)
    
new_list[0].append("Cost")    

for row in new_list[1:]:
    if row[2] != "SELLABLE":
        new_list.remove(row)
    
cost_sum = 0

for n_row in new_list[1:]:
    for c_row in cost_list:
        if str(c_row[0]+"-") in n_row[0] and c_row[1] in n_row[0] and n_row[2] == "SELLABLE":
            n_row.append( round(int(n_row[1]) * float(c_row[2]), 2))
       
qty_sum = 0
cost_sum = 0.00
        
for row in new_list[1:]:
    qty_sum = qty_sum + int(row[1])
    cost_sum = cost_sum + float(row[3])
    
print(qty_sum)
print(round(cost_sum, 2)) 
