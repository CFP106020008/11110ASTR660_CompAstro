import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import simps

D1 = pd.read_fwf('error-mid-1.dat')
D2 = pd.read_fwf('error-mid-2.dat')
D3 = pd.read_fwf('error-trap-1.dat')
D4 = pd.read_fwf('error-trap-2.dat')
D5 = pd.read_fwf('error-Simp-1.dat')
D6 = pd.read_fwf('error-Simp-2.dat')
plt.loglog(D1['N'], D1['Error'], marker='o', label='Midpoint / Single precision', linestyle='dashed', color='C0')
plt.loglog(D2['N'], D2['Error'], marker='o', label='Midpoint / Double precision', linestyle='solid' , color='C0')
plt.loglog(D3['N'], D3['Error'], marker='o', label='Trapezoid / Single precision', linestyle='dashed', color='C1')
plt.loglog(D4['N'], D4['Error'], marker='o', label='Trapezoid / Double precision', linestyle='solid' , color='C1')
plt.loglog(D5['N'], D5['Error'], marker='o', label='Simpson / Single precision', linestyle='dashed', color='C2')
plt.loglog(D6['N'], D6['Error'], marker='o', label='Simpson / Double precision', linestyle='solid' , color='C2')

N = np.logspace(1,7,6)
y1 = N**(-2)
y2 = N**(-4)
plt.loglog(N, y1, linestyle='dotted', color='gray', label='$1/N^2$')
plt.loglog(N, y2, linestyle='dotted', color='k', label='$1/N^4$')

def err3(n):
    x = np.linspace(-1,1,n)
    y = np.sqrt(1-x**2)
    err = abs(simps(y, x)*2 - np.pi)/np.pi
    return err

err_scipy = list(map(err3, N.astype(int) ))
plt.loglog(N, err_scipy, color='skyblue')

plt.xlabel('N')
plt.ylabel('Error')
plt.legend()
plt.tight_layout()
plt.savefig('Convergence.png', dpi=300)
#plt.show()


