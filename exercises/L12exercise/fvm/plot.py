import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

frames = np.arange(0,900,100)

for frame in frames:
	f = pd.read_fwf('Shock_Capturing_Method/advection_%05d.d'%frame)
	plt.plot(f['x'],f['U(x)'],label='%03d'%frame)
	plt.legend()

plt.xlabel("x")
plt.ylabel("U(x)")
#plt.title("finite volume method by Lax-F method")
#plt.savefig("Lax_Friedrichs_method.png",dpi=300)
plt.title("finite volume method by shock-capturing method")
plt.savefig("shock_capturing_method.png",dpi=300)
plt.show()
