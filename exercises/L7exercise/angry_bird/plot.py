import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

RK4     = pd.read_fwf('rk4.dat'  , header=None)
RK2     = pd.read_fwf('rk2.dat'  , header=None)
EULER   = pd.read_fwf('euler.dat', header=None)

plt.plot(EULER.iloc[:,1], EULER.iloc[:,2], label='Euler')
plt.plot(RK2.iloc[:,1]  , RK2.iloc[:,2]  , label='RK2')
plt.plot(RK4.iloc[:,1]  , RK4.iloc[:,2]  , label='RK4')

t = np.linspace(0,10,100)
v = 30
theta = 60
x = v*np.cos(theta*np.pi/180)*t
y = v*np.sin(theta*np.pi/180)*t - 0.5*9.81*t**2
plt.plot(x, y, label='Analytical Solution')

plt.xlim([0,100])
plt.ylim([0,60])
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('$dt = 1$')
plt.legend()
plt.tight_layout()

#plt.show()
plt.savefig('L7Exercise.png', dpi=300)
