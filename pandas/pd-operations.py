#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 20:45:17 2016

@author: tomscott
"""

import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
print(df.head())

print(df['col2'].unique())  # unique items in column
print(df['col2'].nunique())  # number of unique items in column
print(df['col2'].value_counts())  # returns each value in a column and the number of times it occurs

#Select from DataFrame using criteria from multiple columns
newdf = df[(df['col1']>2) & (df['col2']==444)]

df['col1']>2

# apply

def times2(x):
    return x*2
    
df['col1'].apply(times2)
df['col3'].apply(len)

df['col2'].apply(lambda x: x*2)

df.drop('col1', axis=1)  # drop column

# df['col4'].apply(lambda x: 2*x)

# del df['col4']  # permanently delete column

# get index and columns of dataframe

print(df.index)

print(df.columns)

# sorting

df.sort_values(by='col2') #inplace=False by default

# checking for nulls

df.isnull()  # returns a dataframe of booleans



data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)

print(df.pivot_table(values='D',index=['A', 'B'],columns=['C']))  # creates multi-index df








