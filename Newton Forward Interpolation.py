# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:35:58 2026

@author: Student
"""
## Forward Interpolation
import numpy as np
x = np.array([1,2,3,4,5,6])
y = np.array([1,4,9,16,26,37])
n = len(x)
h =x[1] - x[0]
xp = 3.4
u = (xp - x[0])/h
matrix = np.zeros((n,n))

for i in range(n):
    matrix[i][0] = y[i]
    
for j in range(1,n):
    for i in range(n-j):
        matrix[i][j] = matrix[i + 1][j-1] - matrix[i][j-1]
        
print(matrix)

value = matrix[0][0]
U = 1
fact = 1
for p in range(1,n):
    U = U*(u-(p-1))
    fact = fact*p
    value = value + (U*matrix[0][p]) / fact
print(value)

