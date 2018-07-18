# import plotly.plotly as py
# import plotly.graph_objs as go
# import plotly.figure_factory as FF

import math
import numpy as np
import pandas as pd
import matplotlib as mplt
import itertools
#import matplotlib
import matplotlib.pyplot as plt 
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
#matplotlib.tightlayout()
df = pd.read_csv('./fsmstats.csv')
mplt.rc('xtick', labelsize=40) 
mplt.rc('ytick', labelsize=40) 

fsm = (df['FSM'].drop_duplicates().values.tolist())
for i in range(0,len(fsm)):
    filename = fsm[i]
    fsm[i]=fsm[i].split('-')[0]
    if filename == 'halflife2-deathmatch':
        fsm[i] = 'halflife2'
     
avgall = (df['Average all'].drop_duplicates().values.tolist())
stderr = (df['Standard Deviation'].drop_duplicates().values.tolist())

zipped=zip(fsm,avgall,stderr)
zippedsorted = sorted(zipped,key=lambda x: x[1]) 

fsm,avgall,stderr=zip(*zippedsorted)

fig,ax=plt.subplots()
ax.set_xticklabels(fsm,rotation=30,fontsize=30)
plt.ylabel("Average Test Length",fontsize=40)
plt.errorbar(fsm, avgall, stderr, linestyle='None', marker='^', capsize=10,markersize=25) 
#plt.tight_layout()

plt.show()
plt.close()

