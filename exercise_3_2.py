import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#setup plotting preferences
rc={'lines.linewidth': 2, 'axes.labelsize': 18,
'axes.titlesize': 18}
sns.set(rc=rc)

#Set values of scalars
KA = 0.017 #mM^-1
Kd = 0.002 #mM^-1
K_switch = 5.8
wt_R_over_K = 141.5 #mM^-1
q18a_R_over_K = 16.56 #mM^-1
q18m_R_over_K = 1332. #mM^-1


#load data from three files
data_q18m = np.loadtxt('data/q18m_lac.csv', comments='#', skiprows=3, delimiter=',')
data_q18a = np.loadtxt('data/q18a_lac.csv', comments='#', skiprows=3, delimiter=',')
data_wt = np.loadtxt('data/wt_lac.csv', comments='#', skiprows=3, delimiter=',')

#sort x and y data to individual arrays
c_IPTG_q18m = data_q18m[:, 0]
fold_change_q18m = data_q18m[:, 1]
c_IPTG_q18a = data_q18a[:, 0]
fold_change_q18a = data_q18a[:, 1]
c_IPTG_wt = data_wt[:, 0]
fold_change_wt = data_wt[:, 1]

#plot fold change v. log(c) for 3 data sets
plt.semilogx(c_IPTG_q18m, fold_change_q18m, marker='.', linestyle='none',
         markersize=20, alpha=0.5)
plt.semilogx(c_IPTG_q18a, fold_change_q18a, marker='.', linestyle='none',
         markersize=20, alpha=0.5)
plt.semilogx(c_IPTG_wt, fold_change_wt, marker='.', linestyle='none',
         markersize=20, alpha=0.5)
plt.legend(('q18m', 'q18a', 'wt'), loc='lower right')
plt.xlabel('log([IPTG] (mM))')
plt.ylabel('fold change')
