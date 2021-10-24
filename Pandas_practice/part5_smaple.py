# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 21:32:37 2021

@author: dmsal
"""

import pandas as pd

df = pd.DataFrame({'c1':['a', 'a', 'b', 'b', 'b'],
                   'c2':[1, 1, 1, 2, 1],
                   'c3':[1, 1, 2, 2, 2]})

print(df)

col_dup = df['c2'].duplicated()
print(col_dup)
print('\n')

df2 = df.drop_duplicates()
print(df2)
print('\n')