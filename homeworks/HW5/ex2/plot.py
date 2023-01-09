import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

frames = np.arange(0,900,200)

for frame in frames:
	f = pd.read_fwf('Lax_Friedrichs/advection_%05d.d'%frame)
	f1 = pd.read_fwf('Lax_Friedrichs_Gaussian/advection_%05d.d'%frame)
	plt.plot(f['x'],f['U(x)'],label='%03d'%frame)
	plt.plot(f1['x'],f1['U(x)'],linestyle='-.', label='%03d Gaussian'%frame)
	plt.legend()

plt.xlabel("x")
plt.ylabel("U(x)")
#plt.title("finite volume method by Lax-F method")
#plt.savefig("Lax_Friedrichs_method.png",dpi=300)
plt.title("finite volume method by Lax_Friedrichs method")
plt.savefig("LF_Gaussian_average_method.png",dpi=300)
plt.show()
