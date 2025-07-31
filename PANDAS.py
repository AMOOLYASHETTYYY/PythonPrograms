import pandas as pd
import csv
df=pd.read_csv('data.csv')
df.head()
df.tail()

print(df['name'])
print("-------------")
print(df[['name','salary']])
print("-------------")
print(df[df['age']>30])
print("--------------")
print(df.sort_values(by='age'))
print("--------------")
print(df.sort_values(by='age',ascending=False))
print("--------------")
