# -*- coding: utf-8 -*-

import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as mpl

fileName = 'CSVresults/20180209_w_swarm1_circular_uniform_litter.csv'
df = pd.read_csv(fileName)#read csv worldfile

def plotModels(df,modelName,marker,color,ax):
    modelLocations = df[df['name'].str.contains(modelName)]
    modelLocations.plot(kind='scatter',x='x',y='y',ax=ax,label=modelName,color=color,marker=marker)

# set plotting environment
fig,ax = plt.subplots(figsize=(3,3))

#world size is 50m by 50m with bottom,left at -25,-25
boundary = mpl.patches.Rectangle((-25,-25),\
                                         50,50,\
                                         linewidth=2,edgecolor='k',\
                                         facecolor='none',label='boundary')
#ax.add_patch(boundary)


#plot litter objects
plotModels(df,'litter','*',plt.cm.inferno(100),ax)
plotModels(df,'robot','o',plt.cm.inferno(200),ax)

xy = 25
ax.set_ylim([-xy,xy])
ax.set_xlim([-xy,xy])

#ax.set_ylim([-25,25])
#ax.set_xlim([-25,25])
plt.scatter([0],[0],color=plt.cm.inferno(0),label='nest',marker='+',s=100)
#plt.axis('equal')
plt.xlabel('')
plt.ylabel('')
plt.xticks([])
plt.yticks([])

plt.legend(loc='upper center',bbox_to_anchor=(0.5,1.15),ncol=3).remove()
plt.show()
figname = fileName.replace('CSVresults','plots').replace('.csv','-') + str(xy*2) + '.pdf' 
fig.savefig(figname,bbox_inches='tight')