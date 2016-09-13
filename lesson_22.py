import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns

#generate an array of x values
x = np.linspace(-15, 15, 400)

#compute the normalized intensity
norm_I = 4 * (scipy.special.j1(x)/x)**2

#Plot our computation
plt.plot(x, norm_I)
plt.xlabel('$x$')
plt.ylabel('$I(x) / I_0$')
