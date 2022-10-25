import numpy as np
from math import factorial
import matplotlib.pyplot as plt

# factorial(n)=n!
def Method1(x,n):
	return (((-x)**n)/factorial(n))

def Method2(x,n):
	return 1.0 if (n==0) else (((-x)/n)*Method2(x,n-1))

def Method3(x,n):
	return (((x)**n)/factorial(n))

	
N = 100
x = 1.0                #change this value
reale_x = np.exp(-x)

cal1e_x = 0.0
cal2e_x = 0.0
cal3e_x = 0.0

xx = np.zeros(N+1)
x1 = np.zeros(N+1)
x2 = np.zeros(N+1)
x3 = np.zeros(N+1)

ex1 = np.zeros(N+1)
ex2 = np.zeros(N+1)
ex3 = np.zeros(N+1)

relerr1 = np.zeros(N+1)
relerr2 = np.zeros(N+1)
relerr3 = np.zeros(N+1)

# Method 1
for i in range(N+1):
	cal1e_x += Method1(x,i)
	x1[i] = i
	ex1[i] = cal1e_x
	relerr1[i] = abs(cal1e_x-reale_x)/reale_x

# Method 2
for i in range(N+1):
	cal2e_x += Method2(x,i)
	x2[i] = i
	ex2[i] = cal2e_x
	relerr2[i] = abs(cal2e_x-reale_x)/reale_x

# Method 3
for i in range(N+1):
	cal3e_x += Method3(x,i)
	x3[i] = i
	ex3[i] = 1./cal3e_x
	relerr3[i] = abs(ex3[i]-reale_x)/reale_x

# plot the value of e^{-x} as a function of N
plt.plot(x1,ex1,'orange',linewidth=3.5,label="Method 1")
plt.plot(x2,ex2,'k-',label="Method 2")
plt.plot(x3,ex3,'c',label="Method 3")
plt.xlabel("n")
plt.ylabel(r"$e^{-x}$")
plt.title(r"$e^{-x}$ as a function of n steps for x=1.0")
plt.legend()
plt.savefig('ex5_1_value_N.png',dpi=300)
plt.show()

# plot the relative error as a function of N 
plt.plot(x1,np.log10(relerr1),'orange',linewidth=3.5,label="Method 1")
plt.plot(x2,np.log10(relerr2),'k-.',label="Method 2")
plt.plot(x3,np.log10(relerr3),'c:',linewidth=2.5,label="Method 3")
plt.xlabel("n")
plt.ylabel(r"relative error in log10")
plt.title("relative error as a function of n steps for x=1.0")
plt.legend()
plt.savefig('ex5_2_relerr_N.png',dpi=300)
plt.show()
