import pandas as pd
df = pd.read_csv('gym_q1.csv', sep = ";", index_col = 'id', parse_dates = ['date'])
"""
dataframe columns:
id;name;date;height;weight;age;hours;status;children;sex
"""

#Given the dataframe df and using the Pandas library create a function 'solve(df, filename)' that should return a new dataframe created by appending to df the dataframe stored in the file 'filename'. The dataframe in the file has a structure identical to df and should be read with an instruction similar to the one used in the test case to read df.
def solve1(df, filename):
    df2 = pd.read_csv(filename, sep = ";", index_col='id', parse_dates = ['date'])
    df = df.append(df2)
    return df

#Define a solve2 function that should return a new dataframe created by joining to df the columns from the dataframe stored in the file 'filename'. The dataframe in the file has ";" as delimiter and the column "id" should be defined as the index of the dataframe. Only the rows with common "id" in both dataframes shoud be considered.
def solve2(df, filename):
    df2 = pd.read_csv(filename, sep = ";", index_col='id')
    df = df.join(df2)
    return df

"""
dataframe columns:
id;name;date;height;weight;age;hours;status;children;sex;class;city;years;rank
"""

#Define a solve3 function that creates a table with the number of participants by city (row) and class (column) with totals by row and by column
"""It should print something like this:
class       ballet  cycle  hydrogymnastics  pilates  swimming  yoga  zumba  All
city
Gaia           1.0    1.0              NaN      4.0       2.0   1.0    1.0   10
Gondomar       1.0    1.0              NaN      1.0       3.0   NaN    1.0    7
Maia           1.0    2.0              1.0      NaN       4.0   NaN    NaN    8
Matosinhos     NaN    2.0              2.0      1.0       4.0   1.0    NaN   10
Porto          NaN    4.0              2.0      5.0       6.0   NaN    3.0   20
Valongo        NaN    NaN              1.0      NaN       2.0   1.0    1.0    5
All            3.0   10.0              6.0     11.0      21.0   3.0    6.0   60
"""
#It's printing [7 rows x 8 columns] when i don't want to print it

df = pd.read_csv('gym2_q1.csv', sep = ";", index_col = 'id', parse_dates = ['date'])
def solve3():
    df2 = df.groupby(['city', 'class']).size().unstack()
    df2['All'] = df2.sum(axis=1)
    df2.loc['All'] = df2.sum()
    print(df2.head(7))
    
def solve4():
    print(df[df['date'] > pd.Timestamp('2014-12-31')].pivot_table(index='status',columns='sex',values='name',aggfunc='count'))

#Print a dataframe with the number of registered clients by month.
"""It should print something like this:
       clients
month
1            3
2            4
3            3
4            2
5            4
6            5
7            3
8           10
9            8
10           9
11           8
12           1
"""
#instead of printing date it should print month
def solve5():
    df2 = df.groupby(df['date'].dt.month).size().to_frame('clients')
    #rename date column month
    df2.columns = df2.columns.str.replace('date', 'month')
    print(df2)

solve5()
