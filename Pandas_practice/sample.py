# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 17:47:44 2021

@author: dmsal
"""

import pandas as pd
import numpy as np

student1 = pd.Series({'국어': 100, '영어':62, '수학': 70})
student2 = pd.Series({'영어':np.NaN, '수학': 88, '과학': 80})

sr_add = student1.add(student2, fill_value = 0)
sr_sub = student1.sub(student2, fill_value = 0)
sr_mul = student1.mul(student2, fill_value = 0)
sr_div = student1.div(student2, fill_value = 0)

result = pd.DataFrame([sr_add, sr_sub, sr_mul, sr_div],
                      index = ['덧셈', '뺄셈', '곱셈', '나눗셈'])

print(result)