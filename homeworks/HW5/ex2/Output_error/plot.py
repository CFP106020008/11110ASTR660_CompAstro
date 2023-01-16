import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

LF50 = pd.read_fwf('LF_N50_00080.d')
LW50 = pd.read_fwf('LW_N50_00080.d')

LF500 = pd.read_fwf('LF_N500_00080.d')
LW500 = pd.read_fwf('LW_N500_00080.d')

LF5000 = pd.read_fwf('LF_N5000_00080.d')
LW5000 = pd.read_fwf('LW_N5000_00080.d')

N50 = 50.
N500 = 500.
N5000 = 5000.

tot_errLF_50 = np.sum(abs(LF50['U(x)']-LF50['UA(x)']))
tot_errLF_500 = np.sum(abs(LF500['U(x)']-LF500['UA(x)']))
tot_errLF_5000 = np.sum(abs(LF5000['U(x)']-LF5000['UA(x)']))
tot_errLW_50 = np.sum(abs(LW50['U(x)']-LW50['UA(x)']))
tot_errLW_500 = np.sum(abs(LW500['U(x)']-LW500['UA(x)']))
tot_errLW_5000 = np.sum(abs(LW5000['U(x)']-LW5000['UA(x)']))

ave_LF_50 = tot_errLF_50/N50
ave_LF_500 = tot_errLF_500/N500
ave_LF_5000 = tot_errLF_5000/N5000
ave_LW_50 = tot_errLW_50/N50
ave_LW_500 = tot_errLW_500/N500
ave_LW_5000 = tot_errLW_5000/N5000

LF = np.array(np.log10([ave_LF_50,ave_LF_500,ave_LF_5000]))
LW = np.array(np.log10([ave_LW_50,ave_LW_500,ave_LW_5000]))
N = np.log10(np.array([N50,N500,N5000]))

# dt = abs(dx/c)*CFL=abs(1/N)*0.4, c=1, CFL=0.4, N=50,500,5000
# N increases -> dt dexreases -> error decreases
# error is proportional to dt and dx but inversely proportional to N
x = np.log10(np.arange(50.,5000.,1.))
y1 = -1.*(x-N[0])+LF[0]
y2 = -2.*(x-N[0])+LW[0]

plt.plot(N,LF,'-o',label="LF")
plt.plot(N,LW,'-o',label="LW")
plt.plot(x,y1,'k--',label=r"$dt(N^{-1})$")
plt.plot(x,y2,color='gray',linestyle='dashed',label=r"${dt}^2(N^{-2})$")
plt.legend()
plt.xlabel("log(N)")
plt.ylabel(r"log($\epsilon$)")
plt.savefig("logN_logerror.png",dpi=200)
plt.show()
