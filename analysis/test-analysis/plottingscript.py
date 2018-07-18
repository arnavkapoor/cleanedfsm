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
csvresults = sys.argv[1] 
#neededfiles = ['aim.fsm','battlefield2.fsm','counterstrike-source.fsm','halflife2-deathmatch.fsm','dns.fsm','h323.fsm','hotline.fsm','ntp.fsm','rtp.fsm','ssl.fsm','tsp.fsm','yahoo.fsm']
for filename in os.listdir(csvresults):
    print(filename)
    df = pd.read_csv(os.path.join(csvresults,filename))
    testcases=(df['Percentage'].values.tolist())
    x = df['Length'].values.tolist()
    bmk = filename.split('.')[0]
    
    plt.bar(x,testcases,align='center')
    plt.xticks(np.arange(x[0], x[-1], step=1))

    plt.ylabel('Percentage of tests', fontsize=10)
    plt.xlabel('Length of Test-cases',  fontsize=10)

    plt.title(bmk,fontsize=15)
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())
    plt.show()
    #plt.savefig('./individualgraphspercent/'+bmk+'.png')
    plt.close()
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
    #fig = gaussian.get_figure()
    #fig.savefig('./individualgraphspercent/'+bmk+"gaussian.png")
    # fig = dict(data=dataPanda,layout=layout)
    # py.image.save_as(fig, './individualgraphs/'+filename+'2.png')

