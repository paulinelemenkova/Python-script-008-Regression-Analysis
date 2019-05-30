#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

# import data
import os
os.chdir('/Users/pauline/Documents/Python')
dfM = pd.read_csv("Tab-Bathy.csv")
sb.set_style('darkgrid')
df = dfM.melt(id_vars=['observ'], 
              value_vars=["profile1", "profile2", "profile3", "profile4", "profile5", 
                          "profile6", "profile7","profile8", "profile9", "profile10",
                          "profile11", "profile12", "profile13", "profile14", "profile15",
                          "profile16", "profile17", "profile18", "profile19", "profile20",
                          "profile21", "profile22", "profile23", "profile24", "profile25"],
              var_name='Profiles', value_name='Depths')
#print(df.head)

g = sb.lmplot(data=df, x="observ", y="Depths", col="Profiles", hue="Profiles", col_wrap=5, 
              fit_reg=True, truncate=True, x_jitter=True, y_jitter=True, scatter=True,
              markers='.', order=2, height=6)
g = (g.set_axis_labels("Observation points", "Depths, m")
     .fig.subplots_adjust(wspace=.04))
#plt.title('Regression Analysis plot for the Mariana Trench bathymetry', y=1.05, fontsize=12, fontfamily='sans-serif')
sb.set(font_scale=3)
plt.tight_layout()
plt.show()

#sb.plt.savefig("turning_angles.png")
#fig = g.get_figure()
#fig.savefig('output.png') 
#plt.savefig("MyPlot.eps", dpi=300) 
#sb_plot.savefig('output.png')


# In[ ]:




