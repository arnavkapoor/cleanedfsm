import math,sys,os
import numpy as np
import pandas as pd
import matplotlib as mplt
import itertools
import matplotlib.pyplot as plt 
from matplotlib import rcParams

mplt.rcParams['ps.useafm'] = True
mplt.rcParams['pdf.use14corefonts'] = True
mplt.rcParams['text.usetex'] = True

rcParams.update({'figure.autolayout': True})
neededfiles = ['keysight.test']
mplt.rc('xtick', labelsize=30) 
mplt.rc('ytick', labelsize=30) 

basepath = sys.argv[1] + '/'

sparse_cpu_padded_val = []
dense_cpu_paddedtransposed_val = []

sparse = []
dense  = []

bmklist = []
totalgpu = []


for filename in neededfiles:
    
    df1 = pd.read_csv(basepath+'sparseresults/padded/'+filename+'.csv')
    df2 = pd.read_csv(basepath+'sparseresults/padded-transposed/'+filename+'.csv')
    
    df3 = pd.read_csv(basepath+'denseresults/unsorted/padded/'+filename+'.csv')
    df4 = pd.read_csv(basepath+'denseresults/unsorted/padded-transposed/'+filename+'.csv')
    
    sparse_cpu_padded = (df1['Total CPU'].values.tolist()[0])
    sparse_gpu_padded = (df1['Execution GPU'].drop_duplicates().values.tolist()[0])   
    
    sparse_cpu_paddedtransposed = (df2['Total CPU'].values.tolist()[0])
    sparse_gpu_paddedtransposed = (df2['Execution GPU'].drop_duplicates().values.tolist()[0])   
    
    dense_cpu_padded = (df3['Total CPU'].values.tolist()[0])
    dense_gpu_padded = (df3['Execution GPU'].drop_duplicates().values.tolist()[0])   
    
    dense_cpu_paddedtransposed = (df4['Total CPU'].values.tolist()[0])
    dense_gpu_paddedtransposed = (df4['Execution GPU'].drop_duplicates().values.tolist()[0])   
    
    sparseval1=(sparse_cpu_padded/sparse_gpu_padded)
    sparseval2=(sparse_cpu_paddedtransposed/sparse_gpu_paddedtransposed)
    
    denseval1=(dense_cpu_padded/dense_gpu_padded)
    denseval2=(dense_cpu_paddedtransposed/dense_gpu_paddedtransposed)
    
    sparse.append(sparseval1)
    sparse.append(sparseval2)

    dense.append(denseval1)
    dense.append(denseval2)



    bmk = filename.split('.')[0]
    bmk = bmk.split('-')[0]
    bmklist.append(bmk)


fig,ax = plt.subplots()
ind = np.arange(2)
width=0.25

p1 = ax.bar(ind,sparse, width, color='g')
p2 = ax.bar(ind+width,dense, width, color='g',alpha=0.55)

ax.set_xticks(ind + (0.5*width))
ax.set_xticklabels(('padded','padded-transposed'),rotation=15,fontsize=30)
ax.set_yticks(np.arange(1,6,step=1))

ax.axhline(y=1,color='k',ls='dotted')
plt.show()
