#!/usr/bin/env python
# coding: utf-8
import os
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb

os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Bathy.csv")

sb.set_style('darkgrid')
sb.set_context('paper')

# plotting
fig, ax = plt.subplots(1, 5, sharex=True, sharey=True,
                       figsize=(10.0, 4.0), dpi=300
                       )
fig.suptitle('Regression analysis plot: Mariana Trench bathymetry',
             fontsize=10, fontweight='bold', x=0.5, y=0.97
             )
sb.regplot(x="observ", y="profile11", data=df, marker=".", ax=ax[0])
sb.regplot(x="observ", y="profile12", data=df, marker=".", ax=ax[1])
sb.regplot(x="observ", y="profile13", data=df, marker=".", ax=ax[2])
sb.regplot(x="observ", y="profile14", data=df, marker=".", ax=ax[3])
sb.regplot(x="observ", y="profile15", data=df, marker=".", ax=ax[4])

plt.subplots_adjust(wspace=0.05, left=0.025, bottom=0.1, right=0.9, top=0.9)

# visualizing
plt.tight_layout()
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95,
                    hspace=0.25, wspace=0.35)
plt.savefig('plot_RegrAn.png', dpi=300)
plt.show()
