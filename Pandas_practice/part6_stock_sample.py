# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 12:31:09 2021

@author: dmsal
"""

import pandas as pd

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 20)
pd.set_option('display.unicode.east_asian_width', True)

df1 = pd.read_excel('./stock price.xlsx')
df2 = pd.read_excel('./stock valuation.xlsx')

merge_left = pd.merge(df1, df2, how = 'left', left_on='stock_name', right_on= 'name')
print(merge_left)

print('\n')

merge_right = pd.merge(df1, df2, how = 'right', left_on='stock_name', right_on= 'name')
print(merge_right)