#!/usr/bin/env python
# coding: utf-8

# In[76]:


import seaborn as sb
from matplotlib import pyplot as plt
import pandas as pd
import os
os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Bathy.csv")

sb.set_style('darkgrid')

fig, ax = plt.subplots(1, 5, sharex=True, sharey=True, )
sb.regplot(x="observ", y="profile11", data=df, marker=".", ax=ax[0])
sb.regplot(x="observ", y="profile12", data=df, marker=".", ax=ax[1])
sb.regplot(x="observ", y="profile13", data=df, marker=".", ax=ax[2])
sb.regplot(x="observ", y="profile14", data=df, marker=".", ax=ax[3])
sb.regplot(x="observ", y="profile15", data=df, marker=".", ax=ax[4])

plt.subplots_adjust(wspace=0.05, left=0.025, bottom=0.1, right=0.9, top=0.9)

plt.show()
fig.savefig('yourfilename.png')
