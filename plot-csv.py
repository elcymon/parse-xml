# -*- coding: utf-8 -*-

import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as mpl

fileName = 'CSVresults/20180209_w_swarm1_circular_uniform_litter.csv'
df = pd.read_csv(fileName)#read csv worldfile

def plotModels(df,modelName,color,ax):
    modelLocations = df[df['name'].str.contains(modelName)]
    modelLocations.plot(kind='scatter',x='x',y='y',ax=ax,label=modelName,color=color)

# set plotting environment
fig,ax = plt.subplots()

#world size is 50m by 50m with bottom,left at -25,-25
boundary = mpl.patches.Rectangle((-25,-25),\
                                         50,50,\
                                         linewidth=2,edgecolor='k',\
                                         facecolor='none',label='boundary')
ax.add_patch(boundary)


#plot litter objects
plotModels(df,'litter','r',ax)
plotModels(df,'robot','b',ax)

ax.set_ylim([-30,30])
ax.set_xlim([-30,30])
plt.axis('square')

plt.legend(loc='upper center',bbox_to_anchor=(0.5,1.15),ncol=3)
