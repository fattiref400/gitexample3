import numpy as np
import pandas as pd

df = pd.DataFrame([[4, 5, 6, 7],[2,1,0,0]], index=[0, 1],columns=['a','b','c','d'])
print()
print('Data Frame = ')
print(df)
print()

#print('Sum=',df.sum(columns=['a','b']))
print('Sum=')
print(df.sum())
print()
#print('Sum=')
#print(df.sum(columns=['a','b'],index=[1]))
#print()

