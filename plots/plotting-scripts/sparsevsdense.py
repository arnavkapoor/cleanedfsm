# import plotly.plotly as py
# import plotly.graph_objs as go
# import plotly.figure_factory as FF

import math,sys,os
import numpy as np
import pandas as pd
import matplotlib as mplt
import itertools
import matplotlib.pyplot as plt 
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
neededfiles = ['aim.test','battlefield2.test','counterstrike-source.test','dns.test','h323.test','halflife2-deathmatch.test','hotline.test','ntp.test','rtp.test','ssl.test','tsp.test','yahoo.test']
names = ['padded','with-offset','padded-transposed','padded unsorted','with-offset unsorted','padded-transposed unsorted']
mplt.rc('xtick', labelsize=30) 
mplt.rc('ytick', labelsize=30) 

basepath = sys.argv[1]

char1densegpu = []
char1sparsegpu = []

bmklist = []
totalgpu = []


for filename in neededfiles:
    df1 = pd.read_csv(basepath+'sparseresults/'+filename+'.csv')
    df2 = pd.read_csv(basepath+'denseresults/unsorted/padded/'+filename+'.csv')
    
    sparsecpuchar1_16 = (df1['Total CPU'].values.tolist()[1])
    sparsegpuchar1 = (df1['Execution GPU'].drop_duplicates().values.tolist()[0])   
    

    cpuchar1_16 = (df2['Total CPU'].values.tolist()[1])
    gpuchar1 = (df2['Execution GPU'].drop_duplicates().values.tolist()[0])   
    
    char1densegpu.append(cpuchar1_16/gpuchar1)
    char1sparsegpu.append(sparsecpuchar1_16/sparsegpuchar1)
    
    
    bmk = filename.split('.')[0]
    bmk = bmk.split('-')[0]
    bmklist.append(bmk)

zipped=zip(bmklist,char1sparsegpu,char1densegpu)    
zippedsorted=sorted(zipped, key=lambda x: x[2])    

bmklist,char1sparsegpu,char1densegpu=zip(*zippedsorted)


N = len(bmklist)
fig,ax = plt.subplots()
ind = np.arange(N)
width=0.25

print(max(char1densegpu))
print(min(char1densegpu))

p1 = ax.bar(ind,char1sparsegpu, width, color='g',hatch='//')
p2 = ax.bar(ind+width,char1densegpu, width, color='g',alpha=0.55)

ax.set_xticks(ind + (0.5*width))
ax.set_xticklabels(bmklist,rotation=28,fontsize=28)
ax.set_yticks(np.arange(1,5,step=1))

ax.legend((p1[0], p2[0]), ('Sparse','Dense'),fontsize=35)
ax.axhline(y=1,color='k',ls='dotted')
plt.ylabel("Speed up compared to 16-core CPU",fontsize=35)
plt.show()
