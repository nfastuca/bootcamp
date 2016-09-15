import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import hacker_stats as hs
sns.set()

bee_weight = pd.read_csv('data/bee_weight.csv', comment='#')
bee_sperm = pd.read_csv('data/bee_sperm.csv', comment='#')

p_weights = bee_weight.loc[(bee_weight['Treatment'] == 'Pesticide'), 'Weight']
c_weights = bee_weight.loc[(bee_weight['Treatment'] == 'Control'), 'Weight']
x_pw, y_pw = hs.ecdf(p_weights)
x_cw, y_cw = hs.ecdf(c_weights)

plt.plot(x_pw, y_pw, marker='.', linestyle='none', markersize=10, alpha=0.5)
plt.plot(x_cw, y_cw, marker='.', linestyle='none', markersize=10, alpha=0.5)
plt.xlabel('Bee Weight', size=20)
plt.ylabel('ECDF', size=20)
plt.legend(('Pesticide', 'Control'), loc='lower right', fontsize=12)
plt.show()
