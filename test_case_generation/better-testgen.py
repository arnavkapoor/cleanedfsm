import sys
import itertools
import os
from collections import deque
prefixdict = {}
prefixlist = []

outputdir=sys.argv[3]

with open(sys.argv[2],'r') as prefixfile:
    prefixdata=prefixfile.readlines()

for i in range(0,len(prefixdata)):
    prefixlist.append(prefixdata[i].strip().split())

for elements in prefixlist:
    if len(elements)>1:
        prefixdict[elements[0]]=elements[1]
    else:
        prefixdict[elements[0]]=""

namefile=(sys.argv[1].rsplit('/',1)[1])
filewrite= open(os.path.join(outputdir+'/transition_pair_tests',namefile),"w")
count = 1
with open(sys.argv[1], 'r') as myfile1: # the fsm file
    for line in myfile1:
        line = line.strip().split()
        if(len(line)==4):
            line[1] = int(line[1],base=10)    
            line[2] = int(line[2],base=10) 
            try:
                testcase=prefixdict[str(line[1])]+line[0]
                filewrite.write(str(count) + " " + testcase + '\n' )
                count+=1
            except:
                pass    
