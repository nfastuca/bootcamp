import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns

#generate an array of x values
x = np.linspace(-15, 15, 400)

#compute the normalized intensity
norm_I = 4 * (scipy.special.j1(x)/x)**2

#Plot our computed data points with markers, no line
plt.plot(x, norm_I, marker='.', linestyle='none')

#expand margins by 2%
plt.margins(0.02)
plt.xlabel('$x$')
plt.ylabel('$I(x) / I_0$')

#processing the spike data
data = np.loadtxt('data/retina_spikes.csv', skiprows=2, delimiter=',')
t = data[:,0]
V = data[:,1]

#close all other plots just in case
plt.close()
plt.plot(t, V)
plt.xlabel('t (ms)')
plt.ylabel('V (V * 10$^{-6}$)')
plt.xlim(1395, 1400)
