import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

BISEC = pd.read_fwf('bisection.txt')
NEWTON = pd.read_fwf('newton.txt')
SECANT = pd.read_fwf('secant.txt')

plt.semilogy(BISEC['N'], BISEC['Error'], color='C0', marker='o', label='Bisection')
plt.semilogy(NEWTON['N'], NEWTON['Error'], color='C1', marker='o', label='Newton')
plt.semilogy(SECANT['N'], SECANT['Error'], color='C2', marker='o', label='Secant')
plt.legend()
plt.xlabel('N')
plt.ylabel('Error')
plt.savefig('Method_Comparison.png', dpi=200)
plt.show()



