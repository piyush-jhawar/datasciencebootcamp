import numpy as np
import pandas as pd
from numpy.random import randn
from sqlalchemy import create_engine


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

#6 Group By
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)
print(df)
byComp = df.groupby('Company')
print(byComp.mean())
print(byComp.sum())
print(byComp.std())
print(byComp.sum().loc['FB'])
print(df.groupby('Company').sum().loc['FB'])
print(df.groupby('Company').count())
print(df.groupby('Company').describe())

#7 Merging Joining and Concatening

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])

print(pd.concat([df1,df2,df3]))
print(pd.concat([df1,df2,df3],axis=1))

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

print(pd.merge(left,right,how='inner',on='key'))

#8 Operations

df = pd.DataFrame({'col1':[1,2,3,4],
                   'col2':[444,555,666,444],
                   'col3':['abc','def','ghi','xyz']
                   })
print(df.head())
print(df['col2'].unique())
print(df['col2'].nunique())
print(df['col2'].value_counts())

print(df[df['col1']>2])

def times2(x):
    return x*2
print(df['col1'].apply(times2))
print(df['col2'].apply(lambda x : x*2))

# print(df.drop('col1',axis=1))
print(df.index.names)
print(df.columns)
print(df.index)
print(df.sort_values(by='col2'))
print(df.isnull())
print()

data = {'A':['foo','foo','foo','bar','bar','bar'],
        'B':['one','one','two','two','one','one'],
        'C':['x','y','x','y','x','y'],
        'D':[1,3,2,5,4,1]}
df = pd.DataFrame(data)
print(df)
print(df.pivot_table(values='D',index=['A','B'],columns=['C']))

#9 Data Input and Output
#CSV Excel HTML SQL
#Path = /Users/piyushjhawar/PycharmProjects/datasciencebootcamp/section6/
print(pd.read_csv('example.csv'))
print()
print(pd.read_excel('Excel_Sample.xlsx',sheetname='Sheet1'))

df = pd.read_csv('example.csv')
df.to_excel('pandastutorial.xlsx',index=False,sheet_name='Pandastutor')
df.to_csv('pandastutorial.csv',index=False)

# df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
# print(df[0])

engine = create_engine('sqlite:///:memory:')

df.to_sql('my_table',engine)
print()
sqldf = pd.read_sql('my_table',con=engine)
print(sqldf)