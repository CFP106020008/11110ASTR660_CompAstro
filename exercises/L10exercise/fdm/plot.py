import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

frames = np.arange(0,1750,10)

fig, ax = plt.subplots()

for frame in frames:
    D = pd.read_fwf('advection_{:05d}.d'.format(frame))
    ax.plot(D['x'], D['U(x)'], c='b', linestyle='solid')
    ax.plot(D['x'], D['UA(x)'], c='skyblue', linestyle='dotted')
    fig.savefig('images/frame_{:04d}.jpg'.format(frame), dpi=300)
    ax.cla()


