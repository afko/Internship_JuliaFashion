# -*- coding: utf-8 -*-

##### FUNCTION AND MODULE IMPORT #####

import csv

def cost_allocate(f_list, t_list):    
    trans_list[0].append("cost")
    
    for f_row in f_list:
        for t_row in t_list:
            if str(f_row[0] + "-") in t_row[2] and f_row[1] in t_row[2]:
                t_row.append(float(t_row[3]) * float(f_row[2]))
    return t_list

def order_extract(r_list):
    
    new_list = []
    new_list.append(trans_list[0])
    for row in r_list:
        if row[1] == "Order" and row[2] != "":
            new_list.append(row)
    return new_list

##### ANNABELLE STYLE COST CSV IMPORT
f = open ('C:\\Users\data1\Desktop\\transcost.csv' , "r" , encoding = 'utf8')

file = csv.reader(f)

file_list = []

for file_row in file:
    file_list.append(file_row)
    
    

##### TRANSACTION CSV IMPORT
#file_name = input("What is csv file name? ")

#f_trans = open ("C:\\Users\data1\Desktop\\trans\\" + str(file_name) , "r" )

f_trans = open ("C:\\Users\data1\Desktop\\trans\\2017Oct1-2017Oct24CustomTransaction.csv" , "r" )
file_trans = csv.reader(f_trans)

trans_list = []

for trans_row in file_trans:
    temp_list = []
    temp_list.append(trans_row[0])
    temp_list.append(trans_row[2])
    temp_list.append(trans_row[4])
    temp_list.append(trans_row[6])
    temp_list.append(trans_row[21])
    trans_list.append(temp_list)


    
result_list = cost_allocate(file_list, trans_list)
final_list = order_extract(result_list)

qty_sum = 0
total_sum = 0
cost_sum = 0

need_update_list = []
for sum_row in final_list:
    if sum_row == final_list[0]:
        next
    else:
        qty_sum = qty_sum + float(sum_row[3])
        total_sum = total_sum + float(sum_row[4])
        try:
            cost_sum = cost_sum + float(sum_row[5])
        except Exception as exc:
            need_update_list.append(sum_row[2])
            
if len(need_update_list) >= 1:
    print("Check styles what don't have cost for updating.")
        
print (round(qty_sum, ))
print (round(total_sum, 3))
print (round(cost_sum, 3))
