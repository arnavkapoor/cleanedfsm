# import plotly.plotly as py
# import plotly.graph_objs as go
# import plotly.figure_factory as FF

import math
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
neededfiles = ['aim.test','battlefield2.test','counterstrike-source.test','dns.test','h323.test','halflife2-deathmatch.test','hotline.test','ntp.test','rtp.test','ssl.test','tsp.test','yahoo.test']
plt.rc('legend',**{'fontsize':40})

names2 = ['padded','padded-transposed','with-offsets']

names = ['unsorted','sorted']

mplt.rc('xtick', labelsize=30) 
mplt.rc('ytick', labelsize=30) 

#maxpadded = []
#offset = []

#char1cpu = []
#char1gpu = []

maxpaddednosort = []
offsetnosort = []
char1nosort = []

maxpaddedsort = []
offsetsort = []
char1sort = []


bmklist = []

for filename in neededfiles:
    df1 = pd.read_csv('./char1unsorted/'+filename+'.csv')
    df2 = pd.read_csv('./maxpaddingunsorted/'+filename+'.csv')
    df3 = pd.read_csv('./offsetunsorted/'+filename+'.csv')
   
    df4 = pd.read_csv('./individualcsvsortedchar1/'+filename+'.csv')
    df5 = pd.read_csv('./individualcsvsortedmaxpadded/'+filename+'.csv')
    df6 = pd.read_csv('./individualcsvsortedoffset/'+filename+'.csv')
    
    df7 = pd.read_csv('./individualcsvcpusortedminimum/'+filename+'.csv')
    


    cpuchar1 = (df7['Total Time'].values.tolist()[1])
    cpumaxpadded = (df2['Total CPU'].values.tolist()[1])
    cpuoffset = (df3['Total CPU'].values.tolist()[1])
    #cpuchar4 = (df4['Total CPU'].values.tolist()[3])
    gpuchar1 = (df1['Execution GPU'].values.tolist()[0])   
    gpumaxpadded = (df2['Execution GPU'].values.tolist()[0])   
    gpuoffset = (df3['Execution GPU'].values.tolist()[0])   
    
    maxpaddednosort.append(cpumaxpadded/gpumaxpadded)
    char1nosort.append(cpuchar1/gpuchar1)
    offsetnosort.append(cpuoffset/gpuoffset)
  	

    cpuchar1 = (df7['Total Time'].values.tolist()[1])
    cpumaxpadded = (df5['Total CPU'].values.tolist()[1])
    cpuoffset = (df3['Total CPU'].values.tolist()[1])
    #cpuchar4 = (df4['Total CPU'].values.tolist()[3])
    gpuchar1 = (df4['Execution GPU'].values.tolist()[0])   
    gpumaxpadded = (df5['Execution GPU'].values.tolist()[0])   
    gpuoffset = (df6['Execution GPU'].values.tolist()[0])   
    
    #gpuchar4 = (df4['Execution GPU'].drop_duplicates().values.tolist()[0])   
     
    #maxpadded.append(cpumaxpadded/gpumaxpadded)
    maxpaddedsort.append(cpumaxpadded/gpumaxpadded)
    char1sort.append(cpuchar1/gpuchar1)
    offsetsort.append(cpuoffset/gpuoffset)
    
    #offset.append(cpuoffset/gpuoffset)

    # df1 = pd.read_csv('./individualcsvchar1/'+filename+'.csv')
    # df2 = pd.read_csv('./individualcsvoffset/'+filename+'.csv')
    # df3 = pd.read_csv('./individualcsvmaxpadded/'+filename+'.csv')
    
    # cpuchar1 = (df1['Total CPU'].values.tolist()[3])
    # cpumaxpadded = (df2['Total CPU'].values.tolist()[3])
    # cpuoffset = (df3['Tot.3al CPU'].values.tolist()[3])
    # #cpuchar4 = (df4['Total CPU'].values.tolist()[3])
    

    # gpuchar1 = (df1['Execution GPU'].drop_duplicates().values.tolist()[0])   
    # gpuoffset = (df2['Execution GPU'].drop_duplicates().values.tolist()[0])   
    # gpumaxpadded = (df3['Execution GPU'].drop_duplicates().values.tolist()[0])   
    # #gpuchar4 = (df4['Execution GPU'].drop_duplicates().values.tolist()[0])   
   

    bmk = filename.split('.')[0]
    bmk = bmk.split('-')[0]
    bmklist.append(bmk)
    #totalgpu.append( timecpu1/(df['Total GPU'].drop_duplicates().values.tolist()[0]))
zipped=zip(bmklist,maxpaddednosort,char1nosort,offsetnosort,maxpaddedsort,char1sort,offsetsort)    
zippedsorted=sorted(zipped, key=lambda x: x[-2])    

bmklist,maxpaddednosort,char1nosort,offsetnosort,maxpaddedsort,char1sort,offsetsort=zip(*zippedsorted)

N = len(bmklist)
fig,ax = plt.subplots()
ind = np.arange(N)
width=0.25
maxpaddedsort=list(maxpaddedsort)
char1sort=list(char1sort)
offsetsort=list(offsetsort)

maxpaddednosort=list(maxpaddednosort)
char1nosort=list(char1nosort)
offsetnosort=list(offsetnosort)


print(maxpaddednosort,offsetnosort,bmklist)

p1 = ax.bar(ind,maxpaddednosort, width, color='#009292')
p2 = ax.bar(ind+width,char1nosort, width, color='#490092')
p3 = ax.bar(ind+2*width,offsetnosort, width, color='#888888',hatch='//')

for i in range(0,len(maxpaddedsort)):
    maxpaddedsort[i] = maxpaddedsort[i] - maxpaddednosort[i]
    char1sort[i] = char1sort[i] - char1nosort[i]
    offsetsort[i] = offsetsort[i] - offsetnosort[i]


p4 = ax.bar(ind,maxpaddedsort, width,bottom=maxpaddednosort, color='#009292',alpha=0.60)
p5 = ax.bar(ind+width,char1sort, width,bottom=char1nosort, color='#490092',alpha=0.60)
p6 = ax.bar(ind+2*width,offsetsort, width,bottom=offsetnosort, color='#888888',alpha=0.50,hatch='//')

# p5 = ax.bar(ind+4
# p5 = ax.bar(ind+4*width,offsetnosort, width, color='m')
# p6 = ax.bar(ind+5*width,char1nosort, width, color='c')

#ax.set_title('Speed-up in Execution Time',fontsize=15)

ax.set_xticks(ind + width)
ax.set_xticklabels(bmklist,rotation=28,fontsize=35)

legend1=plt.legend((p1[0], p4[0]), (names),title=names2[0],fontsize=40,loc=(0.02,0.70))
legend2=plt.legend((p2[0], p5[0]), (names),title=names2[1],fontsize=40,loc=(0.25,0.70)) 
legend3=plt.legend((p3[0],p6[0]), (names),fontsize=40,title=names2[2],loc=(0.49,0.70))

legend1.set_title(names2[0],prop={'size':35})
legend2.set_title(names2[1],prop={'size':35})
legend3.set_title(names2[2],prop={'size':35})
ax.axhline(y=1,color='k',ls='dotted')
ax.set_yticks(np.arange(1,13,step=1))


plt.gca().add_artist(legend1)
plt.gca().add_artist(legend2)
plt.gca().add_artist(legend3)

plt.ylabel("Speed up compared to 16-core CPU",fontsize=40)
plt.show()
plt.close()


