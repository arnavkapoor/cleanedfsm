import os,sys
from pathlib import Path

rawfsm = sys.argv[1] 
cleanedfsm = sys.argv[2]

for file in os.listdir(rawfsm):
    fsmdata = []
    with open(os.path.join(rawfsm,file), 'r') as fsmfile:
        fsmdata=fsmfile.readlines()

    filewrite = open(os.path.join(cleanedfsm,file),"w")
    fsm = []
    print(file)
    for i in range(0,len(fsmdata)):
        fsm.append(fsmdata[i].strip().split())
    
    numstates = 0    
    numtransitions = 0
    
    numtransitions = len(fsm)
    for elements in fsm:
        # CAREFUL: Assumes that state enumeration starts from 1
        numstates = max(numstates,int(elements[1]),int(elements[2]))
        if(elements[0] == "\\"):
            elements[0]= r'\\'
            print(elements)        
    filewrite.write(".i 1"+'\n')
    filewrite.write(".o 1"+'\n')
    filewrite.write(".s "+str(numstates)+'\n')
    filewrite.write(".p "+str(numtransitions)+'\n')
    filewrite.write(".b 10" + '\n')

    for elements in fsm:
        if(len(elements)==4):   
            filewrite.write(elements[0] + " " + elements[1] + " " + elements[2] + " "+ elements[3] + '\n')
