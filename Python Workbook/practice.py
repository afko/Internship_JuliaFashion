# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:06:40 2017

@author: Data1
"""

import csv

f = open("C:\\Users\data1\Desktop\data-master\data-master\\nfl-suspensions\\nfl-suspensions-data.csv", "r")
f_reader = csv.reader(f)

nfl_suspensions = []
for row in f_reader:
    nfl_suspensions.append(row)


class Suspensions:
    def __init__(self, data):
        self.data = data
        self.name = data[0]
        self.team = data[1]
        self.games = data[2]
        self.year = data[5]

nfl = Suspensions(nfl_suspensions[3])
print (nfl)

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except Exception as exc:
            self.year = 0
            
    def get_year(self):
        return(self.year)
        
missing_year = Suspension(nfl_suspensions[23])
missing_year.get_year()

