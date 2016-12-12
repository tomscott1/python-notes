#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 20:16:48 2016

@author: tomscott
"""

import pandas as pd

df = pd.read_csv('example')

df2 = pd.read_excel('Excel_Sample.xlsx', sheetname='Sheet1')
