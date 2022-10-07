import numpy as np
import matplotlib.pyplot as plt

# Define the equations

def Eq1(x, h):
    Eq1 = ((np.cos(x+h) - np.cos(x)) - (np.cos(x) - np.cos(x-h)))/h**2
    return Eq1

def Eq2(x, h):
    Eq2 = (np.cos(x+h)+np.cos(x-h)-2*np.cos(x))/h**2
    return Eq2

# Define relative errors
# Note that d^2/dx^2 cos(x) = -cos(x)

def eps1(x, h):
    epsilon1 = abs((Eq1(x, h) + np.cos(x))/np.cos(x))
    return epsilon1

def eps2(x, h):
    epsilon2 = abs((Eq2(x, h) + np.cos(x))/np.cos(x))
    return epsilon2

# Define the range of h we want to use
N = np.logspace(0,6,30)
h = np.pi/N

# Visualize the results
plt.plot(np.log10(h), np.log10(eps1(1,h)), label='Equation 1')
plt.plot(np.log10(h), np.log10(eps2(1,h)), label='Equation 2')
plt.xlim(np.log10(h[0]), np.log10(h[-1]))
plt.xlabel('$\log_{10}h$')
plt.ylabel('$\log_{10}\epsilon$')
plt.legend()
plt.tight_layout()
plt.savefig('Derivative.png', dpi=300)
