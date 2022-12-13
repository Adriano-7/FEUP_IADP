import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('supermarket1.csv', sep=';')

def solve1():
    df.drop('Customer type', axis=1, inplace=True)

def solve2():
    df1 = df.groupby('Product line')['Quantity'].sum()
    df2 = df1.reset_index()
    df3 = df2.append({'Product line': 'All', 'Quantity': df1.sum()}, ignore_index=True)
    df4 = df3.set_index('Product line')
    print(df4)

#it's not working
def solve3():
    df1 = df.groupby(['City', 'Customer type'])['Invoice ID'].count()
    df2 = df1.reset_index()
    df3 = df2.pivot(index='City', columns='Customer type', values='Invoice ID')
    df4 = df3.append(df3.sum().rename('All'))
    df5 = df4.fillna(0).astype(int)
    df6 = df5.rename_axis(None, axis=1)
    print(df6)

#it's not working
def solve4():
    df1 = df.groupby(['City', 'Customer type'])['Invoice ID'].count()
    df2 = df1.reset_index()
    df3 = df2.pivot(index='City', columns='Customer type', values='Invoice ID')
    df4 = df3.append(df3.sum().rename('All'))
    df5 = df4.fillna(0).astype(int)
    print(df5)

def solve5():
    df1 = df.groupby(['City', 'Product line'])['Total'].sum()
    df2 = df1.reset_index()
    df3 = df2.sort_values(by='Total', ascending=False)
    df4 = df3.groupby(['City', 'Product line']).head(1)
    df5 = df4.reset_index()
    df6 = df5[['City', 'Product line', 'Total']]
    df7 = df6.round(2)
    print(df7.iloc[df7['Total'].idxmax(), 0], df7.iloc[df7['Total'].idxmax(), 1], df7.iloc[df7['Total'].idxmax(), 2], sep=', ')

def solve6():
    df.columns = df.columns.str.replace(' ', '_')

def solve7():
    df1 = df['Total'].describe()
    df2 = df1.round(2)
    print(df2)

def solve8():
    df.drop(df[df['City'] == 'Yangon'].index, inplace=True)

#It's not working, it's returning KeyError: 'Unit_price'
def solve9():
    df.insert(9, 'QxPrice', df['Unit_price'] * df['Quantity'])
    
def solve10():
    df1 = df[df['Total'] > 1030]
    df2 = df1[['Product line', 'Unit price', 'Quantity', 'Tax 5%', 'Total']]
    print(df2)

def solve11():
    df1 = df.loc[0:2, 'Total':'Payment']
    print(df1)

def solve12():
    df1 = df['Total']
    df2 = pd.cut(df1, bins=[0, 220, 440, 660, 880, 1100], labels=['low', 'fair', 'good', 'very_good', 'excellent'])
    df3 = df2.value_counts()
    print(df3)

def solve13():
    df.loc[2, 'Customer type'] = 'Member'

def solve14():
    df1 = df['Product line'].value_counts()
    print(df1)

#It's not working
def solve15():
    df1 = df.loc[0:2, 'Invoice ID':'Total']
    df2 = df1[['Invoice ID', 'Total']]
    df2.drop(df2.index[1], inplace=True)
    print(df2)

#It's not working
def solve16():
    print("")
    

def solve17():
    df1 = df.groupby(['City', 'Payment'])['Total'].sum()
    df2 = df1.reset_index()
    df3 = df2.pivot(index='City', columns='Payment', values='Total')
    df4 = df3.round(2)
    print(df4)

def solve18():
    df1 = df[df['Customer_type'] == 'Female']
    df2 = df1['Total'].mean()
    df3 = df2.round(1)
    print(df3)