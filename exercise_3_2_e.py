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

#experimental data as a list
experimental_y = [fold_change_wt, fold_change_q18a, fold_change_q18m]
experimental_x = [c_IPTG_wt, c_IPTG_q18a, c_IPTG_q18m]

#range for theoretical values
bohr_par_range = np.linspace(-6, 6, 100)

def bohr_parameter(c, R_to_K, Kd=Kd, KA=KA, K_switch=K_switch):
    log_arg = (1 + c/KA)**2 / ((1 + c/KA)**2 + K_switch*(1 + c/Kd)**2)

    return -np.log(R_to_K) - np.log(log_arg)


def fold_change_bohr(bohr_parameter):
    """

    """
    out = (1+ np.exp(-bohr_parameter))**(-1)
    return out

bohr_dist = fold_change_bohr(bohr_par_range)

#for each R_to_K, convert c to par
bohrs = []
for c, val in zip(experimental_x, RK):
    par = bohr_parameter(c, val)
    bohrs.append(par)

#plot theoretical curve
plt.plot(bohr_par_range, bohr_dist, color='gray')

#plot data sets
for x, y, l in zip(bohrs, experimental_y, labels):
    plt.plot(x, y, color=colors[l], marker='.', markersize=20, linestyle='none', alpha=0.5)

plt.show()
