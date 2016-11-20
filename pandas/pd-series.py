#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 11:30:51 2016

@author: tomscott
"""

import pandas as pd
import numpy as np

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}

s1 = pd.Series(data=my_data)
s2 = pd.Series(data=my_data, index=labels)
s3 = pd.Series(arr, labels)  # shorthand
s4 = pd.Series(d)
s5 = pd.Series(labels)  # series of strings
s6 = pd.Series(data=[sum,print,len])  # series of functions 

ser1 = pd.Series([1,2,3,4], ['USA','Germany','USSR', 'Japan'])
ser2 = pd.Series([1,2,5,4], ['USA','Germany','Italy', 'Japan'])

ser1['USA']  # 1

s5[0]  # 'a'
