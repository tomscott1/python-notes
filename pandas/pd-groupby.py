#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 19:45:07 2016

@author: tomscott
"""
import numpy as np
import pandas as pd


data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)

df1 = df.groupby('Company')
df1.mean()  # on numeric columns
df1.sum()
df1.std()

