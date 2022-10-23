import numpy as np
import matplotlib.pyplot as plt

N = np.logspace(0,7,50)

def etot(em):
    return N**(-2) + em*N**0.5

plt.loglog(N, etot(1e-7), label='32 bit')
plt.loglog(N, etot(1e-15), label='64 bit')
plt.legend()
plt.xlabel('N')
plt.ylabel(r'$\epsilon_{\rm tot}$')
plt.tight_layout()
plt.savefig('demo.png', dpi=200)
plt.show()





