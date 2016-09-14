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

def fold_change(R_to_K, KA=KA, Kd=Kd, K_switch=K_switch):
    """
    Generates theoretical values for fold_change(concentration)
    over range of c covering experimental data
    """

    c = np.logspace(np.log10(np.min(c_IPTG_q18m)), np.log10(np.max(c_IPTG_q18m)),
                    num=100)
    fold_change_model = 1/(1+(R_to_K*((1 + c /KA))**2)/((1 + (c / KA))**2 +
    K_switch*(1 + (c / Kd)**2)))
    return c, fold_change_model

#iterate fold_change(R_to_K) over list of R/K values, appends output to empty
#list
fold_change_models = []
for val in RK:
    c, fold_change_model = fold_change(val)
    fold_change_models.append(fold_change_model)


#plot fold change v. log(c) for 3 data sets
#***optimize to be included in other plot loop***
plt.semilogx(c_IPTG_q18m, fold_change_q18m, marker='.', linestyle='none',
         markersize=20, alpha=0.5, color=colors['q18m'])
plt.semilogx(c_IPTG_q18a, fold_change_q18a, marker='.', linestyle='none',
         markersize=20, alpha=0.5, color=colors['q18a'])
plt.semilogx(c_IPTG_wt, fold_change_wt, marker='.', linestyle='none',
         markersize=20, alpha=0.5, color=colors['wt'])

#Loop through list of output data from fold_cange(R_to_K) and plot
#***optimize to append tuples to use in plt.legend***
for y, l in zip(fold_change_models, labels):
    plt.semilogx(c, y, color=colors[l])

plt.legend(('q18m', 'q18a', 'wt', 'wt model', 'q18a model', 'q18m_model'),
           loc='lower right')
plt.xlabel('log([IPTG] (mM))')
plt.ylabel('fold change')
