# import plotly.plotly as py
# import plotly.graph_objs as go
# import plotly.figure_factory as FF

import math,os,sys
import numpy as np
import pandas as pd
import matplotlib as mplt
import itertools
import matplotlib.pyplot as plt 
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

neededfiles = []
names = ['padded','padded-transposed','with-offsets']
mplt.rc('xtick', labelsize=30) 
mplt.rc('ytick', labelsize=30) 

#maxpadded = []
#offset = []

#char1cpu = []
#char1gpu = []
basefolder = sys.argv[1] + '/'
for folder, sub_folders, files in os.walk(basefolder+'unsorted/'+'padded-transposed/'):
    for special_file in files:
        file_path = os.path.join(folder, special_file)
        splits = special_file.split('.')
        neededfiles.append(splits[0]+"."+splits[1])
maxpaddednosort = []
offsetnosort = []
char1nosort = []
bmklist = []

for filename in neededfiles:
   
    df1 = pd.read_csv(basefolder+'unsorted/'+'padded-transposed/'+filename+'.csv')
    df2 = pd.read_csv(basefolder+'unsorted/'+'padded/'+filename+'.csv')
    df3 = pd.read_csv(basefolder+'unsorted/'+'with-offsets/'+filename+'.csv')
  
    
    cpuchar1 = (df1['Total CPU'].values.tolist()[1])
    cpumaxpadded = (df2['Total CPU'].values.tolist()[1])
    cpuoffset = (df3['Total CPU'].values.tolist()[1])
    #cpuchar4 = (df4['Total CPU'].values.tolist()[3])
    gpuchar1 = (df1['Execution GPU'].drop_duplicates().values.tolist()[0])   
    gpumaxpadded = (df2['Execution GPU'].drop_duplicates().values.tolist()[0])   
    gpuoffset = (df3['Execution GPU'].drop_duplicates().values.tolist()[0])   
   
    maxpaddednosort.append(cpumaxpadded/gpumaxpadded)
    char1nosort.append(cpuchar1/gpuchar1)
    offsetnosort.append(cpuoffset/gpuoffset)
    
    if filename == 'halflife2-deathmatch.test':
        filename = 'halflife2.test'
    bmk = filename.split('.')[0]
    bmk = bmk.split('-')[0]
    bmklist.append(bmk)
    print(bmk,gpuchar1,gpuoffset)
   
zipped=zip(bmklist,maxpaddednosort,char1nosort,offsetnosort)    
zippedsorted=sorted(zipped, key=lambda x: x[2])    

bmklist,maxpaddednosort,char1nosort,offsetnosort=zip(*zippedsorted)

N = len(bmklist)
fig,ax = plt.subplots()
ind = np.arange(N)
width=0.25


p1 = ax.bar(ind,maxpaddednosort, width, color='#009292')
p2 = ax.bar(ind+width,char1nosort, width, color='#490092')
p3 = ax.bar(ind+2*width,offsetnosort, width, color='#888888',hatch='//')

ax.set_yticks(np.arange(1,9,step=1))

ax.set_xticks(ind + width)
ax.set_xticklabels(bmklist,rotation=28,fontsize=28)
ax.legend((p1[0], p2[0],p3[0]), (names),fontsize=35)
ax.axhline(y=1,color='k',ls='dotted')

plt.ylabel("Speed up compared to 16-core CPU",fontsize=35)
plt.show()
plt.close()


