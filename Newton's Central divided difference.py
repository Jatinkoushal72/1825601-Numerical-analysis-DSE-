import numpy as np
x = np.array([1,2,3,4,5,6])
y = np.array([1,4,9,16,26,37])
n = len(x)
xp = 3.4
matrix = np.zeros((n,n))

for i in range(n):
    matrix[i][0] = y[i]
    
for j in range(1,n):
    for i in range(n-j):
        matrix[i][j] = (matrix[i + 1][j-1] - matrix[i][j-1])/(x[i+j] - x[i])
        
print(matrix)

value = matrix[0][0]
U = 1
for p in range(1,n):
    U = U*(xp - x[p-1])
    value = value + (U*matrix[0][p])
print(value)
    

