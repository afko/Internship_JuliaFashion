# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 11:44:30 2017

@author: Data1
"""

import pandas as pd

sales_data = pd.read_excel("C:\\Users\data1\OneDrive - JULIA\Glamit J\\Template\\Report_Template.xlsm")
sales_data.columns = sales_data.iloc[1]

sales_data = sales_data[2:]

