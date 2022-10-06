import numpy as np
import matplotlib.pyplot as plt

x,y = np.loadtxt("pi_error.dat",unpack=True)
plt.plot(np.log10(x),np.log10(y),marker='o', linestyle='dashed')
plt.xlabel("log(N)")
plt.ylabel("relative error log(e)")
plt.savefig("pi_error_AAFO_loge.png")
plt.show()

