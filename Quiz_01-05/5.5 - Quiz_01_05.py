import numpy as np

#Given the initial, final, and the number of values (all floats) generate an array with n elements between initial and final values equally spaced, square the values and calculate the sum (rounded to two decimal places), using NumPy library.

initial = float(input("Initial value:"))
final = float(input("Final value:"))
n = int(input("Number of values:"))

#generate an array with n elements between initial and final values equally spaced
m = np.linspace(initial, final, n)
#square the values
m = m ** 2
#calculate the sum
print("Sum of the array:", round(np.sum(m), 2))


#Given the number of rows and columns, generate a numpy array with values given by the user.
rows = int(input("Number of rows:"))
columns = int(input("Number of columns:"))

m = np.array([[int(input(f"a[{i}, {j}]=")) for j in range(columns)] for i in range(rows)], dtype = float)
np.transpose(m)
print("Matrix transpose:")
for i in range(columns):
    print(m.T[i])

#Compute the sum of two NxM matrices using NumPy library.
rows = int(input())
columns = int(input())
m1 = np.array([[int(x) for x in input().split(",")] for i in range(rows)], dtype = float)
m2 = np.array([[int(x) for x in input().split(",")] for i in range(rows)], dtype = float)

#sum the two using numpy
m = m1 + m2
for i in range(rows):
    print(m[i])