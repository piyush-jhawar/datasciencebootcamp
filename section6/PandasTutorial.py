import numpy as np
import pandas as pd
from numpy.random import randn


#1 Introduction to Pandas
#2 Series
labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}


print(pd.Series(data=my_data))
print(pd.Series(data=my_data,index=labels))
print(pd.Series(arr,labels))
print(pd.Series(d))

ser1 = pd.Series([1,2,3,4],index=['USA','Germany','USSR','Japan'])
print(ser1)
ser2 = pd.Series([1,2,5,4],index=['USA','Germany','Italy','Japan'])
print(ser2)
print(ser1['USA'])
ser3 = pd.Series(data=labels)
print(ser3[0])

#3 DataFrames - Part1
np.random.seed(101)

df = pd.DataFrame(randn(5,4),index=list('ABCDE'),columns=  ['W','X','Y','Z'])
# print (df)
print(df['W'])
print(df.W)
print(df[['W','Z']])
df['new'] = df['W'] + df['Y']
print(df)
df.drop('new',axis=1,inplace=True)
print(df)
#ROWS
print(df.loc['A'])
print(df.iloc[2])
print(df.loc['B','Y'])
print(df.loc[['A','B'],['W','Y']])

#4 DataFrames - Part2
np.random.seed(101)

df = pd.DataFrame(randn(5,4),index=list('ABCDE'),columns=  ['W','X','Y','Z'])
print(df[df['W'] > 0])

print(df[df['W']>0]['X'])
print()
print(df[(df['W']>0) & (df['Y']>1)])
print(df[(df['W']>0) | (df['Y']>1)])
print(df.reset_index())
newind = 'CA NY WY OR CO'.split()
df["states"] = newind
print(df.set_index('states'))

#4 DataFrames - Part3
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
print()
print(df.loc['G1'].loc[1])


print(df.index.names)
print(df.columns.name)
print(df.xs('G1'))
print(df.xs(1,level=1))

#5 Missing Data

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)
print(df)
print(df.dropna())
print(df.dropna(thresh=2))
print(df.fillna(value=df[['A','B','C']].mean()))
