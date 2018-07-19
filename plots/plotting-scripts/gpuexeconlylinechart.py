# import plotly.plotly as py
# import plotly.graph_objs as go
# import plotly.figure_factory as FF
import sys,os
import math
import numpy as np
import pandas as pd
import matplotlib as mplt
import itertools
import matplotlib.pyplot as plt 

mplt.rc('xtick', labelsize=30) 
mplt.rc('ytick', labelsize=30) 

linestyles = ['-', ':', '-.', '--']
markers = ['x', '^', 'o', '*']
handlestyles = itertools.product(linestyles, markers)    
total = 0
handles = []
labels = []
sortingpoints = []
fig, ax = plt.subplots()
ax.set_xscale('log', basex=2,subsx=(2,3,4,5,6,7,8,9,10))  

path = sys.argv[1]

for folder, sub_folders, files in os.walk(path):
    for special_file in files:
        file_path = os.path.join(folder, special_file)
        df = pd.read_csv(file_path)
        #df2 = pd.read_csv('./individualcsvcpusortedminimum/'+filename+'.csv')
        testcases=(df['Testcases'].drop_duplicates().values.tolist())
        totalcpu = (df['Total CPU'].values.tolist())

  
        totalcpu32=[]
        totalcpu16=[]
        totalcpu8=[]
        totalcpu1=[]
        bmk = special_file.split('.')[0]
        bmk = bmk.split('-')[0]
        
        
        for i in range(0,len(totalcpu)):
            if(i%4==0):
                totalcpu32.append(totalcpu[i])
            if(i%4==1): 
                totalcpu16.append(totalcpu[i])
            if(i%4==2):
                totalcpu8.append(totalcpu[i])
            if(i%4==3):
                totalcpu1.append(totalcpu[i])

        myindices = []

        executiongpupre = (df['Execution GPU'].values.tolist())
        totalgpupre = (df['Total GPU'].values.tolist())
        
        for i in range(0,len(executiongpupre)):
            if i%4 == 0:
                myindices.append(i)

        executiongpu  = [ executiongpupre[i] for i in myindices ]  
        totalgpu  = [ totalgpupre[i] for i in myindices ]       
        print(len(totalcpu1),len(executiongpu))
        for i in range(0,len(executiongpu)):
            executiongpu[i] = totalcpu16[i]/executiongpu[i]
        print(executiongpu[0],bmk)    
        total+=executiongpu[0]
        
        handlestyle = next(handlestyles)
        handle,=plt.plot(testcases,executiongpu,label=bmk,linestyle=handlestyle[0],marker=handlestyle[1],markersize=13)
        handles.append(handle)
        labels.append(bmk)
        sortingpoints.append(executiongpu[0])


print(total/12)

#plt.ticklabel_format(style = 'plain',labelsize=20)
plt.ylabel('Speed up compared to 16-core CPU',fontsize=35)
plt.xlabel('Number of tests (log base 2)',fontsize=35)
#plt.xticks([np])    #sort the labels/handles by the sorting points
sortingpoints, labels, handles = zip(*sorted(zip(sortingpoints, labels, handles), key=lambda t: t[0], reverse=True))
    #set the legend
plt.legend(loc = 2, fontsize = 25, labels=labels, handles=handles,fancybox=True, framealpha=0.2)
#plt.title(bmk,fontsize=15)
manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())
#plt.savefig('./newsetofgraphs/'+'dense2char1'+'.pdf',bbox_inches='tight')
plt.show()
#plt.close()
    #plt.show()    
    # layout ={
    #         'title':filename,
    #         'yaxis': {
    #         'title' : 'Testcases/second'
    #         },
    #         'xaxis': {
    #         'title' : 'Log Number of Testcases'
    #         },
    #  }

    # fig = dict(data=dataPanda,layout=layout)
    # py.image.save_as(fig, './individualgraphs/'+filename+'2.png')

