import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


f = pd.read_fwf('2d_advection/advection_00800.d')
U = np.array(f['U(x,y)']).reshape(128,128)

fig, ax = plt.subplots()
im = ax.imshow(U,origin='lower',extent=[0,1,0,1])
cbar = ax.figure.colorbar(im)
cbar.ax.set_ylabel("U(x,y)", rotation=-90, va="bottom")
ax.set_title("2d advection at tend")
plt.savefig("2d_advection_tend.png", dpi=200)
plt.show()

