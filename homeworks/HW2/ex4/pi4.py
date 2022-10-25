import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

N = np.logspace(1,6,6).astype(int)

def func(x):
    return np.sqrt(1 - x**2)
    #return x**4

#ans = 2/5
ans = np.pi/2
#ans = (2+np.pi)/2

def Simpson(N):
    dx = 2/N
    A = 0
    for i in range(N):
        x1 = -1 + dx*i
        x2 = -1 + dx*(i+1)
        h1 = func(x1)
        h2 = func((x2+x1)/2)
        h3 = func(x2)
        A += (h1+4*h2+h3)*dx/6
    return A

def Trap(N):
    dx = 2/N
    A = 0
    for i in range(N):
        x1 = -1 + dx*i
        x2 = -1 + dx*(i+1)
        h1 = func(x1)
        h2 = func(x2)
        A += (h1+h2)*dx/2
    return A

def err1(n):
    return abs((Simpson(n)-ans)/(ans))
def err2(n):
    return abs((Trap(n)-ans)/ans)

y0 = N.astype(float)**(-1.5)
y1 = N.astype(float)**(-2)
y2 = N.astype(float)**(-4)
plt.loglog(N, y0, linestyle='dotted', color='#a0a0a0', label='$1/N^{1.5}$')
plt.loglog(N, y1, linestyle='dotted', color='gray', label='$1/N^2$')
plt.loglog(N, y2, linestyle='dotted', color='k', label='$1/N^4$')

def err3(n):
    x = np.linspace(-1,1,n)
    y = func(x)
    err = abs(simps(y, x) - ans)/ans
    return err

#err_scipy = list(map(err3, N.astype(int) ))
#plt.loglog(N, err_scipy, color='skyblue', label='Scipy Simps')
errs1 = list(map(err1, N))
errs2 = list(map(err2, N))
plt.loglog(N, errs1, label='Simpson')
plt.loglog(N, errs2, label='Trapezoid')
plt.legend()
plt.xlabel('N')
plt.ylabel('$\epsilon$')
plt.title('Integrate $\sqrt{2-x^2}$ from -1 to 1')
plt.savefig('1-x2.png')
#plt.show()

