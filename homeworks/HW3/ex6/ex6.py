import numpy as np
import time
import scipy
from scipy.linalg import lu
from scipy.linalg import solve_banded

###############################
#(a)
# solve by lu
n = 100
A = np.zeros((n,n))
b = np.ones((n,1))

for i in range(n):
    for j in range(n):
        if (i==j):
            A[i][j] = 6.
        elif (abs(i-j)==1):
            A[i][j] = -4.
        elif (abs(i-j)==2):
            A[i][j] = 1.

A[0][0] = 9.
A[-1][-1] = 1.
A[-2][-1] = -2.
A[-1][-2] = -2.
A[-2][-2] = 5.

start = time.time()
p, L, U = lu(A)
y = np.linalg.inv(L) @ b
x_a = np.linalg.inv(U) @ y
end = time.time()

print("(a)")
print("computing time = %f s by LU" %(end-start))

# solve by solve_banded
l = 2
u = 2
A_b = np.zeros((l+u+1,n))

for i in range(n):
    for j in range(n):
        if ( i == j):
            A_b[l][j] = A[i][j]
            
        elif ( i-j == -1):
            A_b[l-1][j] = A[i][j]
        
        elif ( i-j == -2):
            A_b[l-2][j] = A[i][j]
        
        elif ( i-j == 1):
            A_b[l+1][i] = A[i][j]
        
        elif ( i-j == 2):
            A_b[l+2][i] = A[i][j]

start = time.time()
x_b = solve_banded((l, u), A_b, b)
end = time.time()

print("computing time = %f s by solve_banded" %(end-start))

###############################
# (b)
R = np.zeros((n,n))

for i in range(n):
    for j in range(n):
        if (i==j):
            R[i][j] = 1
        elif (j>i and abs(i-j)==1):
            R[i][j] = -2
        elif (j>i and abs(i-j)==2):
            R[i][j] = 1
R[0][0]=2

TorF = np.allclose(A,(R @ R.transpose()))
print("(b)")
print("A=RR^T is ", TorF)


# (c)
cond_A = np.linalg.cond(A)
print("(c)")
print("condition number of A = ", cond_A)

