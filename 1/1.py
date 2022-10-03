import locale
import numpy as np
from numpy.linalg import matrix_power
import math
locale.setlocale(locale.LC_ALL, "ru_RU")
a = math.pi/4
b = math.pi*3/4
lamb = 0.51

h = (b-a)/10

s = []
s.append(a + h/2)
for i in range(1, 10):
    s.append(s[i-1] + h)

def myfunc(i, j):
    return math.sin(s[i]*s[j])*h

print('A')

for i in range(10):
    row = ''
    for j in range(10):
        kek = myfunc(i, j)

        if kek > 0:
            row += locale.str((round(kek, 6))) + ' & '
        else:
            row += locale.str((round(kek, 5))) + ' & '
    row = row[:-2]
    row += '\\\\'
    print(row)
print()
print()
print('E+lambda*A')

matrix = np.zeros((10, 10))
for i in range(10):
    row = ''
    for j in range(10):
        kek = myfunc(i, j)*lamb
        if i==j:
            kek += 1
        matrix[i][j] = kek
        if kek > 0:
            row += locale.str((round(kek, 6))) + ' & '
        else:
            row += locale.str((round(kek, 5))) + ' & '
    row = row[:-2]
    row += '\\\\'
    print(row)

cheb_vector = np.zeros(10)
for i in range(10):
    for j in range(10):
        cheb_vector[i] += abs(matrix[i][j])
print('cheb = ', locale.str((round(max(cheb_vector), 6))))


a = np.zeros(10)
for i in range(10):
    a[i] = 1
vect_b = np.dot(matrix, a)
str = ""
for x in vect_b:
    if x > 0:
        str += locale.str(round(x, 6)) + ' \\\\ '
    else:
        str += locale.str(round(x, 5)) + ' \\\\ '
print("b = ")
print(str)

delta_b = [1, -1, 1 , -1, 1, -1, 1, -1, 1, -1]
for i in range(10):
    delta_b[i] = delta_b[i]*vect_b[i]*0.01

str = ""
for x in delta_b:
    if x > 0:
        str += locale.str(round(x, 6)) + ' \\\\ '
    else:
        str += locale.str(round(x, 5)) + ' \\\\ '
print("delta_b = ")
print(str)

b_full = []
for i in range(10):
    b_full.append(vect_b[i] + delta_b[i])

str = ""
for x in b_full:
    if x > 0:
        str += locale.str(round(x, 6)) + ' \\\\ '
    else:
        str += locale.str(round(x, 5)) + ' \\\\ '
print("full_b = ")
print(str)
matrix_1 = matrix_power(matrix, -1)


print()
print()
print('(E+lambda*A)^-1')
for i in range(10):
    row = ''
    for j in range(10):
        kek = matrix_1[i][j]
        if kek > 0:
            row += locale.str((round(kek, 6))) + ' & '
        else:
            row += locale.str((round(kek, 5))) + ' & '
    row = row[:-2]
    row += '\\\\'
    print(row)


cheb_vector = np.zeros(10)
for i in range(10):
    for j in range(10):
        cheb_vector[i] += abs(matrix_1[i][j])
print('cheb_1 = ', locale.str((round(max(cheb_vector), 6))))


full_x = np.dot(matrix_1, b_full)
str = ""
for x in full_x:
    if x > 0:
        str += locale.str(round(x, 6)) + ' \\\\ '
    else:
        str += locale.str(round(x, 5)) + ' \\\\ '
print("full_x = ")
print(str)

delta_x = []
for i in range(10):
    delta_x.append(full_x[i] - 1)

str = ""
for x in delta_x:
    if x > 0:
        str += locale.str(round(x, 6)) + ' \\\\ '
    else:
        str += locale.str(round(x, 5)) + ' \\\\ '
print("delta_x = ")
print(str)

B = np.zeros((10, 10))
for i in range(10):
    for j in range(10):
        B[i][j] = matrix[i][j]/b_full[i]

print()
print()
print('B')
for i in range(10):
    row = ''
    for j in range(10):
        kek = B[i][j]
        if kek > 0:
            row += locale.str((round(kek, 6))) + ' & '
        else:
            row += locale.str((round(kek, 5))) + ' & '
    row = row[:-2]
    row += '\\\\'
    print(row)

print()
print()
print("B-1")
B_1 = matrix_power(B, -1)
for i in range(10):
    row = ''
    for j in range(10):
        kek = B_1[i][j]
        if kek > 0:
            row += locale.str((round(kek, 6))) + ' & '
        else:
            row += locale.str((round(kek, 5))) + ' & '
    row = row[:-2]
    row += '\\\\'
    print(row)

x_prime = np.dot(B_1, a)
str = ""
for x in x_prime:
    if x > 0:
        str += locale.str(round(x, 6)) + ' \\\\ '
    else:
        str += locale.str(round(x, 5)) + ' \\\\ '
print("x_prime = ")
print(str)