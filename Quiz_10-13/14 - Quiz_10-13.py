import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

#df = pd.read_csv('gym2_q1.csv', sep = ";", index_col = 'id', parse_dates = ['date'])

#Given the dataframe df and using the Pandas library create a function 'solve(last_name)' to answer the following: Count and print the number of ocurrences of the last name (last_name).
"""
def solve1(last_name):
    print(f"Number of ocurrences of {last_name}: {df[df['name'].str.contains(last_name)].shape[0]}")
    return
"""

#df = pd.read_csv('gym_q1.csv',sep=';', parse_dates=['date'])

#Given the dataframe df and using the Pandas library create a function 'solve()' to answer the following: Create a new column 'years' with the number of days between 'date' and 1/1/2022 divided by 365 days and converted to an integer. Print the first three rows of the dataframe. 
"""
def solve2():
    df['years'] = (datetime.datetime(2022,1,1) - df['date']).dt.days / 365
    df['years'] = df['years'].astype(int)
    print(df.head(3))
    return

solve2()
"""

#df = pd.read_csv('gym2_q1.csv', sep = ";", index_col = 'id', parse_dates = ['date'])
#Given the dataframe df and using the Pandas library create a function 'solve(old_cat, new_cat)' to answer the following: Change the 'rank'  name from old_cat to new_cat and convert the column 'rank' to category dtype.
"""
def solve3(old_cat, new_cat):
    df['rank'] = df['rank'].replace(old_cat, new_cat)
    df['rank'] = df['rank'].astype('category')
    return

solve3('fair', 'poor')
print(pd.unique(df['rank']))
"""

df = pd.read_csv('gym2_q1_nan.csv', sep = ";", index_col = 'id', parse_dates = ['date'])
"""
Dataframe columns:
id;name;date;height;weight;age;hours;status;children;sex;class;city;years;rank
"""

#Given the dataframe df and using the Pandas library create a function 'solve()' to answer the following: Delete the rows with NaN values in any of the columns. Print the (number rows, number of cols) before and after.

def solve4():
    print(df.shape)
    df.dropna(inplace = True)
    print(df.shape)
    return


#Given the dataframe df and using the Pandas library create a function 'solve()' to answer the following: Print a numpy array with the number of rows that have no NaN values and the number of rows that have at least one NaN value.

def solve5():
    print(np.array([df.dropna().shape[0], df[df.isna().any(axis = 1)].shape[0]]))
    return

solve5()