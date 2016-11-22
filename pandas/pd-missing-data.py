#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 19:38:06 2016

@author: tomscott
"""

import numpy as np
import pandas as pd

d = {'a':[1,2,np.nan],'b':[5,np.nan,np.nan],'c':[1,2,3]}
df = pd.DataFrame(d)

# drop na values

df1 = df.dropna(axis=0)  # default axis = 0 for rows
df2 = df.dropna(axis=1, thresh=2)  # columns/ require 2 NA values

# fill na values

df3 = df.fillna(value='fill')  # fill na with value
df4 = df['a'].fillna(value=df['a'].mean())  # fill column with mean of column

