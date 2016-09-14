import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set()
pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

#Practice 1_a
df.loc[(df['adhesive strength (Pa)'] < -2000), 'impact time (ms)']

#Practice 1_b
 df.loc[df['ID'] == 'II', ['impact force (mN)', 'adhesive force (mN)']]

#Practice 1_c
df.loc[(df['ID'] == 'III') | (df['ID'] == 'IV'), ['time frog pulls on
      target (ms)', 'adhesive force (mN)']]
