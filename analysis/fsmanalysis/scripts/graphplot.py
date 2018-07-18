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

path = sys.argv[1]     # directory containing data  

for folder, sub_folders, files in os.walk(path):
    for special_file in files:
        file_path = os.path.join(folder, special_file)
        print(file_path)
        df = pd.read_csv(file_path)
        testcases=(df['Percentage Transitions'].values.tolist())
        bmk = file_path.split('/')[-1]
        bmk = bmk.split('.')[0]
        print(bmk)
        testcases.sort()
        summ=0
        for i in range(0,len(testcases)):
            summ+=testcases[i]
        try:
            print((summ*100/len(testcases)),filename)
        except:
            pass
        x = [i for i in range(1,len(testcases)+1)]
        plt.bar(x,testcases,align='center')
        plt.ylabel('Transition Percentage', fontsize=10)
        plt.xlabel('States',  fontsize=10)

        plt.title(bmk,fontsize=15)
        manager = plt.get_current_fig_manager()
        manager.resize(*manager.window.maxsize())
        plt.show()
        #plt.savefig(bmk+'.pdf') // to save directly
        plt.close()
