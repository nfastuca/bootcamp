import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')
beak_data = [bd_1975, bd_2012]
data_names = ['bd_1975', 'bd_2012']

def bs_sample(data):
    """
    Generates a bootstap data set from original data
    """
    return np.random.choice(data, replace=True, size=len(data))

def bs_reps(data, n_reps=10000):
    """
    Generates 'n_reps' number of bootstrap data sets from original data and
    appends them to an empty array.  Returns 1-d array of bootstrap data sets
    of shape (n_reps,)
    """
    bs_reps = np.empty(n_reps)
    for i in range(n_reps):
        bs_sample_out = bs_sample(data)
        bs_reps[i] = np.mean(bs_sample_out)
    return bs_reps

def conf_int(data, n_reps=10000, perc=95.):
    """
    Calculates 'perc' $%$ confidence interval for data by running 'n_reps'
    bootstrap experiment replications
    """
    return np.percentile(bs_reps(data, n_reps=n_reps), [((100. - perc)/2),
                        (100 - (100 -perc)/2)])

for set, name in zip(beak_data, data_names):
    perc_95 = conf_int(set)
    print('95"%"confidence interval for', name, ':', perc_95)
#report 95% confidence interval for 1975
# conf_int_1975 = np.percentile(bs_replicates_1975, [2.5, 97.5])

# #generate bootstrap 2012
# n_reps = 100000
# bs_replicates_2012 = np.empty(n_reps)
# for i in range(n_reps):
#     bs_sample = np.random.choice(bd_2012, replace=True, size=len(bd_2012))
#     bs_replicates_2012[i] = np.std(bs_sample)
#
# #report 95% confidence interval for 2012
# conf_int_2012 = np.percentile(bs_replicates_2012, [2.5, 97.5])
#
#
# def ecdf(data):
#     return np.sort(data), np.arange(1, len(data) + 1) / len(data)
#
# print('conf_int_1975 = ', conf_int_1975, 'conf_int_2012 = ', conf_int_2012)

# x_1975, y_1975 = ecdf(bd_1975)
# x_2012, y_2012 = ecdf(bd_2012)
# x_1975_bs, y_1975_bs = ecdf(bs_sample)
#

# plt.plot(x_1975, y_1975, marker='.', linestyle='none')
# plt.plot(x_2012, y_2012, marker='.', linestyle='none')
# plt.plot(x_1975_bs, y_1975_bs, marker='.', linestyle='none')
# plt.xlabel('beak depth (mm)')
# plt.ylabel('ECDF')
# plt.legend(('1975', '2012', '1975 bs'), loc='lower right')
# plt.show()
