import locale
import numpy as np
from numpy.linalg import matrix_power
import math
locale.setlocale(locale.LC_ALL, "ru_RU")
a = math.pi/4
b = math.pi*3/4
lamb = -0.5

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


print(sorted(s, reverse=True))
kaks = np.dot(matrix, sorted(s, reverse=True))
print(kaks)
summ_vector = np.zeros(10)
for i in range(10):
    for j in range(10):
        summ_vector[i] += matrix[i][j]
print('summ = ',summ_vector)
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
