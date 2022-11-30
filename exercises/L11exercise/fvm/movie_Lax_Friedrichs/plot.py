import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

frames = np.arange(0,900,10)

for frame in frames:
	f = pd.read_fwf('../Lax_Friedrichs/advection_%05d.d'%frame)
	plt.plot(f['x'],f['U(x)'],label='%05d'%frame)
	plt.legend()
	plt.xlim(0.0,1.0)
	plt.ylim(0.0,1.3)
	plt.xlabel("x")
	plt.ylabel("U(x)")
	plt.savefig("Lax_Friedrichs_%05d.png"%frame,dpi=200)
	plt.clf()
