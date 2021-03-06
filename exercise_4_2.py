import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import hacker_stats as hs
sns.set()

bee_weight = pd.read_csv('data/bee_weight.csv', comment='#')
bee_sperm = pd.read_csv('data/bee_sperm.csv', comment='#')

#Munch data, create df of weight and sperm quality for Pestice and control bees
p_weights = bee_weight.loc[(bee_weight['Treatment'] == 'Pesticide'), 'Weight']
c_weights = bee_weight.loc[(bee_weight['Treatment'] == 'Control'), 'Weight']
p_sperm = bee_sperm.loc[(bee_sperm['Treatment'] == 'Pesticide'), 'Quality'].dropna()
c_sperm = bee_sperm.loc[(bee_sperm['Treatment'] == 'Control'), 'Quality'].dropna()

#generate ecdf datapoints
x_pw, y_pw = hs.ecdf(p_weights)
x_cw, y_cw = hs.ecdf(c_weights)
x_ps, y_ps = hs.ecdf(p_sperm)
x_cs, y_cs = hs.ecdf(c_sperm)

#compute mean weights
p_weight_mean = np.mean(p_weights)
c_weight_mean = np.mean(c_weights)
p_sperm_mean = np.mean(p_sperm)
c_sperm_mean = np.mean(c_sperm)
p_sperm_median = np.median(p_sperm)
c_sperm_median = np.median(c_sperm)


#compute 95% confidence intervals
p_weight_ci= hs.conf_int(p_weights)
c_weight_ci = hs.conf_int(c_weights)
p_sperm_ci = hs.conf_int(p_sperm)
c_sperm_ci = hs.conf_int(c_sperm)
p_sperm_ci_median = hs.conf_int_median(p_sperm)
c_sperm_ci_median = hs.conf_int_median(c_sperm)

#close any open plots
plt.close()


#plot ecdf of weights
plt.plot(x_pw, y_pw, marker='.', linestyle='none', markersize=10, alpha=0.5)
plt.plot(x_cw, y_cw, marker='.', linestyle='none', markersize=10, alpha=0.5)
plt.xlabel('Bee Weight', size=20)
plt.ylabel('ECDF', size=20)
plt.legend(('Pesticide', 'Control'), loc='lower right', fontsize=12)
plt.savefig('bee_weight_ECDF.svg', bbox_inches='tight')
plt.close()

#Plot ecdf of sperm qualities
plt.plot(x_ps, y_ps, marker='.', linestyle='none', markersize=10, alpha=0.5)
plt.plot(x_cs, y_cs, marker='.', linestyle='none', markersize=10, alpha=0.5)
plt.xlabel('Bee Sperm Quality', size=20)
plt.ylabel('ECDF', size=20)
plt.legend(('Pesticide', 'Control'), loc='lower right', fontsize=12)
plt.savefig('bee_sperm_ECDF.svg', bbox_inches='tight')
