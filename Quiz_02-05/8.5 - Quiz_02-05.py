import pandas as pd
df = pd.read_csv('gym_q1.csv',sep=';', parse_dates=['date'])

#Define a function solve() that returns the number of people that train less than 2 hours per week
def solve1():
    print(len(df.loc[df['hours'] < 2]))

#Define a function solve2() that Knowing that the last two digits of the id represent the last two digits of the year of registration, build the list of applicants in 2013 aged 50 years or over. View id, name, weight, height and age.
def solve2():
    df['year'] = df['id'].apply(lambda x: str(x)[-2:])
    print(df.loc[(df['year'] == "13") & (df['age'] >= 50), ['id', 'name', 'weight', 'height', 'age']])

#Define a function solve3() that prints the average age of people who train more than 5 hours a week (rounded to two decimal places).
def solve3():
    hey = round(df.loc[df['hours'] > 5, 'age'].mean(),2)
    print(f"{hey:.2f}")


#Define a function solve4() that prints the total number of children of customers over 55 years of age.
def solve4():
    print(df.loc[df['age'] > 55, 'children'].sum())

#Define a function solve5() that prints the most common number of children among customers.
def solve5():
    print(df['children'].value_counts().idxmax())
