# import plotly.plotly as py
# import plotly.graph_objs as go
# import plotly.figure_factory as FF
import csv,os,sys
import math
import numpy as np
import pandas as pd
import matplotlib as mplt
import itertools
import matplotlib.pyplot as plt 

csvresultsdir = sys.argv[1]
fsmfilenamecsv = sys.argv[2]

file = csv.writer(open(fsmfilenamecsv,'w'))
file.writerow(['FSM', 'Median', 'Standard Deviation' ,'Variance','Average all','Total all'])        

for filename in os.listdir(csvresultsdir):
    
    df = pd.read_csv(os.path.join(csvresultsdir,filename))

    freq =df['Number'].values.tolist()
    val = df['Length'].values.tolist()
    bmk = filename.split('.')[0]
    data = np.repeat(val, freq)
    tsumtot=0
    
    for ele in data:
        tsumtot+=ele
        
    file.writerow([bmk,np.median(data),np.std(data),np.var(data),np.average(data),tsumtot])
  
