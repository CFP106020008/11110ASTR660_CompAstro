'''
This code is used to calculate pi using Monte Carlo method.
Author: Lin Yen-Hsing (NTHU) 2022.10.07
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def cal_pi(N):
    np.random.seed(111)
    x = np.random.random(N)
    np.random.seed(222)
    y = np.random.random(N)
    r = np.sqrt(x**2 + y**2)
    PI = np.sum(r<1)/np.shape(r)[0]*4
    print(PI)
    return PI

def err(N):
    ERR = abs((cal_pi(N) - np.pi)/np.pi)
    return ERR

def expect(N,a):
    return a/np.sqrt(N)

N = np.logspace(1, 7, 20).astype(int)
Errs = list(map(err, N))

popt, pcov = curve_fit(expect, N, Errs)

plt.loglog(N, Errs, label='Simulated data', linestyle='solid')
plt.loglog(N, expect(N, popt[0]), label='Expected $1/\sqrt{N}$ law', linestyle='dashed')

plt.xlabel('$N$')
plt.ylabel('$\epsilon$')
plt.legend()
plt.tight_layout()
plt.savefig('pi_MC.png', dpi=300)

plt.show()



