#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 15:52:59 2016

@author: tomscott
"""

import numpy as np
import pandas as pd
from numpy.random import randn

# part 1

np.random.seed(101)  # set random generator seed

df = pd.DataFrame(randn(5,4),['a','b','c','d','e'],['w','x','y','z'])

# selecting columns

df['w']  # returns column 'w' as a series
df[['w','z']]  # returns list of columns in dataframe format

# creating new columns
df['new'] = df['w'] + df['y']

# dropping columns
df.drop('new', axis = 1, inplace=True) 
# axis = 1 refers to columns not index (axis = 0)
# inplace occurs on the df 

# drop rows
df.drop('e')  # axis = 0 by default

# selecting rows
df.loc['b']  # returns row 'b'
df.iloc[1]  # returns row 'b'

# subsets of rows and columns
df.loc['b','y']
df.loc[['a','b'],['w','y']]

# part 2

# conditional selection

booldf = df > 0
df[booldf]

# one step
df[df>0]

df['w'] > 0  # returns T/F depending on value in the column

df[df['w']>0]  # removes any rowns in 'w' that are false

# re-index

newind = 'CA NY WY OR CO'.split()
df['States'] = newind
df.set_index('States')

# part 3












