import matplotlib.pylab as plt
import numpy as np
from numpy import loadtxt
from scipy.interpolate import interp1d

m3corr50, Prat1_50 = np.loadtxt('ratio50.csv', delimiter=' ',
                                dtype=float, usecols=(0,1), unpack=True)
m3corr60, Prat1_60 = np.loadtxt('ratio60.csv', delimiter=' ',
                                dtype=float, usecols=(0,1), unpack=True)
m3corr70, Prat1_70 = np.loadtxt('ratio70.csv', delimiter=' ',
                                dtype=float, usecols=(0,1), unpack=True)
m3corr80, Prat1_80 = np.loadtxt('ratio80.csv', delimiter=' ',
                                dtype=float, usecols=(0,1), unpack=True)
m3corr90, Prat1_90 = np.loadtxt('ratio90.csv', delimiter=' ',
                                dtype=float, usecols=(0,1), unpack=True)
m3corr100, Prat1_100 = np.loadtxt('ratio100.csv', delimiter=' ',
                                  dtype=float, usecols=(0,1), unpack=True)
## SI CONVETION
m3corr50 = m3corr50 *.4536
m3corr60 = m3corr60 *.4536
m3corr70 = m3corr70 *.4536
m3corr80 = m3corr80 *.4536
m3corr90 = m3corr90 *.4536
m3corr100 = m3corr100 *.4536

Prat2_50, effC_50 = np.loadtxt('efficiency50.csv', delimiter=' ',
                               dtype=float, usecols=(0,1), unpack=True)
Prat2_60, effC_60 = np.loadtxt('efficiency60.csv', delimiter=' ',
                               dtype=float, usecols=(0,1), unpack=True)
Prat2_70, effC_70 = np.loadtxt('efficiency70.csv', delimiter=' ',
                               dtype=float, usecols=(0,1), unpack=True)
Prat2_80, effC_80 = np.loadtxt('efficiency80.csv', delimiter=' ',
                               dtype=float, usecols=(0,1), unpack=True)
Prat2_90, effC_90 = np.loadtxt('efficiency90.csv', delimiter=' ',
                               dtype=float, usecols=(0,1), unpack=True)
Prat2_100, effC_100 = np.loadtxt('efficiency100.csv', delimiter=' ',
                                 dtype=float, usecols=(0,1), unpack=True)

## SORTING
Prat1_50 = Prat1_50[np.argsort(m3corr50)]
m3corr50 = np.sort(m3corr50)
Prat1_60 = Prat1_60[np.argsort(m3corr60)]
m3corr60 = np.sort(m3corr60)
Prat1_70 = Prat1_70[np.argsort(m3corr70)]
m3corr70 = np.sort(m3corr70)
Prat1_80 = Prat1_80[np.argsort(m3corr80)]
m3corr80 = np.sort(m3corr80)
Prat1_90 = Prat1_90[np.argsort(m3corr90)]
m3corr90 = np.sort(m3corr90)
Prat1_100 = Prat1_100[np.argsort(m3corr100)]
m3corr100 = np.sort(m3corr100)


Prat2_100 = np.sort(Prat2_100)
effC_100 = effC_100[np.argsort(Prat2_100)]
Prat2_90 = np.sort(Prat2_90)
effC_90 = effC_90[np.argsort(Prat2_90)]
Prat2_80 = np.sort(Prat2_80)
effC_80 = effC_80[np.argsort(Prat2_80)]
Prat2_70 = np.sort(Prat2_70)
effC_70 = effC_70[np.argsort(Prat2_70)]
Prat2_60 = np.sort(Prat2_60)
effC_60 = effC_60[np.argsort(Prat2_60)]
Prat2_50 = np.sort(Prat2_50)
effC_50 = effC_50[np.argsort(Prat2_50)]

### TURBINE DATA

m5corr1,PratT = np.loadtxt('ratioT.csv', delimiter=' ',
                           dtype=float, usecols=(0,1), unpack=True)
m5corr1 = m5corr1 *.4536
m5corr2,effT = np.loadtxt('effT.csv', delimiter=' ',
                          dtype=float, usecols=(0,1), unpack=True)
m5corr2 = m5corr2 *.4536

####################################################################
#######PLOTANDO DADOS###############################################
####################################################################
plt.figure(1)
plt.scatter(m3corr50,Prat1_50, label=("Corrected Speed 50"))
plt.scatter(m3corr60,Prat1_60, label=("Corrected Speed 60"))
plt.scatter(m3corr70,Prat1_70, label=("Corrected Speed 70"))
plt.scatter(m3corr80,Prat1_80, label=("Corrected Speed 80"))
plt.scatter(m3corr90,Prat1_90, label=("Corrected Speed 90"))
plt.scatter(m3corr100,Prat1_100, label=("Corrected Speed 100"))
plt.title("Overall Compressor Pressure Ratio Map")
plt.xlabel("Corrected Mass Flow rate Kg/S")
plt.ylabel("P3/P2")
plt.legend(loc="best")
plt.grid()

plt.figure(2)
plt.scatter(Prat2_50,effC_50, label=("Corrected Speed 50"))
plt.scatter(Prat2_60,effC_60, label=("Corrected Speed 60"))
plt.scatter(Prat2_70,effC_70, label=("Corrected Speed 70"))
plt.scatter(Prat2_80,effC_80, label=("Corrected Speed 80"))
plt.scatter(Prat2_90,effC_90, label=("Corrected Speed 90"))
plt.scatter(Prat2_100,effC_100, label=("Corrected Speed 100"))
plt.title("Overall Compressor Efficiency Map")
plt.xlabel("P3/P2")
plt.ylabel("Compressor Efficiency")
plt.legend(loc="best")
plt.grid()

plt.figure(3)
plt.plot(m5corr1,PratT, label=("Corrected Speed Ratio 2.17"))
plt.title("Turbine Pressure Ratio Map")
plt.xlabel("Corrected Mass Flow rate Kg/S")
plt.ylabel("P4/P5")
plt.legend(loc="best")
plt.grid()

plt.figure(4)
plt.plot(m5corr2,effT, label=("Corrected Speed Ratio 2.17"))
plt.title("Turbine Efficiency Map")
plt.xlabel("Corrected Mass Flow rate Kg/S")
plt.ylabel("Turbine Efficiency")
plt.legend(loc="best")
plt.grid()

plt.show()
