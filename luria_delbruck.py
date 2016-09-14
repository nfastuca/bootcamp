import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#Specify parameters
#number of generations
n_gen = 16

#chance of a beneficial mutation
r = 1e-5

#total number of cells
n_cells = 2**(n_gen-1)

# Adaptive immunity:binomial distribution
ai_samples = np.random.binomial(n_cells, r, size=100000)

# Report mean and std
print('AI Mean', np.mean(ai_samples))
print('AI std', np.std(ai_samples))
print('AI Fano', np.var(ai_samples) / np.mean(ai_samples))


def ecdf(data):
    return np.sort(data), np.arange(1, len(data) + 1) / len(data)

#Function to draw out of random mutation hypothesis
def draw_random_mutation(n_gen, r):
    """Draw sample under random mutation hypothesis"""
    # Initialize number of mutations
    n_mut = 0

    for g in range(n_gen):
        n_mut = 2*n_mut + np.random.binomial(2**g - 2*n_mut, r)

    return n_mut

def sample_random_mutation(n_gen, r, size=100000):
    #initialize samples
    samples = np.empty(size)

    #draw samples
    for i in range(size):
        samples[i] = draw_random_mutation(n_gen, r)

    return samples

rm_samples = sample_random_mutation(n_gen, r)

x_ai, y_ai = ecdf(ai_samples)
x_rm, y_rm = ecdf(rm_samples)

print('RM Mean', np.mean(rm_samples))
print('RM std', np.std(rm_samples))
print('RM Fano', np.var(rm_samples) / np.mean(ai_samples))

plt.semilogx(x_ai, y_ai, marker='.', linestyle='none', alpha=0.5)
plt.semilogx(x_rm, y_rm, marker='.', linestyle='none', alpha=0.5)
plt.xlabel('Number of mutants')
plt.ylabel('ECDF')
plt.legend(('Adaptive immunity', 'Random mutation'))
