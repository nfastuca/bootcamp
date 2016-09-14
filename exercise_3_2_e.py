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

#make list of R/K values
RK = [wt_R_over_K, q18a_R_over_K, q18m_R_over_K]

#List of data set names
labels = ['wt', 'q18a', 'q18m']

#Dictionary with colors corresponding to each data set name
colors = {'wt': 'red', 'q18a': 'blue', 'q18m': 'green'}

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

c = np.logspace(np.log10(np.min(c_IPTG_q18a)), np.log10(np.max(c_IPTG_q18a)),
                num=100)

def fold_change_bohr(c, R_to_K, Kd=Kd, KA=KA, K_switch=K_switch):
    lnRK = np.log(R_to_K)
    ln_fraction = np.log(((1 + c/KA)**2)/((1 + c/KA)**2 +
                  (K_switch*(1 + c/Kd)**2)))
    bohr_par = -1*(lnRK + ln_fraction)
    out = (1 + np.exp((-1)*bohr_par))
    return out
