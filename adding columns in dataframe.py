# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 21:17:31 2021

@author: Admin
"""

import pandas as pd
import matplotlib.pyplot as plt

lengths = {'circle': [23,43,54,65,76,81],
        'square': [3,4,5,7,9,11],
        'sphere': [4,5,3,6,7,8]
        }
df = pd.DataFrame(lengths)

df['area of circle'] = 1/2 * 3.142 * (df['circle'])**2
df['area of square'] = df['square']**2
df['volume of sphere'] = 4/3 * 3.142 * df['sphere']**3



print(df)

plt.plot(df)
plt.show()
