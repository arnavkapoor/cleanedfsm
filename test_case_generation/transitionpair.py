import sys
import os


with open(sys.argv[1], 'r') as myfile1: # the fsm file
    fsmdata=myfile1.readlines()

namefile=(sys.argv[1].rsplit('/',1)[1])
outputdir=sys.argv[2]
fsm=[]

filewrite = open(os.path.join(outputdir+'/transition_pairs',namefile),"w")


for i in range(0,len(fsmdata)):
    fsm.append(fsmdata[i].strip().split())


userinput = []
currstate = []
nextstate = []
useroutput = []

visited = []

for ele in fsm:
    
    if(len(ele) == 2):
        if(ele[0] == '.b'):
            base = int(ele[1]) 
        if(ele[0] == '.p'):
            totalcount = int(ele[1])
        if(ele[0] == '.i'):
            inputlen = int(ele[1])
        if(ele[0] == '.o'):
            outputlen = int(ele[1])
                
    if(len(ele)==4):
        userinput.append(ele[0])
        currstate.append(ele[1])
        nextstate.append(ele[2])
        useroutput.append(ele[3])
        visited.append(0)

for i in range(0,len(currstate)):
    currstate[i] = int(currstate[i],base=base) # currstate[i] was initially string,converted to integer   

for i in range(0,len(nextstate)):
    nextstate[i] = int(nextstate[i],base=base)

filewrite.write(".i "+str(2*inputlen)+'\n')
filewrite.write(".o "+str(2*outputlen)+'\n')
filewrite.write(".s 2"+'\n')
filewrite.write(".b 10"+'\n')

inout = {}

for ele in currstate:
    inout[ele]=([],[])
for ele in nextstate:
    inout[ele]=([],[])
    
for i in range(0,len(userinput)):
    
    cs = currstate[i]
    ns = nextstate[i]
    ip = userinput[i]
    op = useroutput[i]

    inout[cs][1].append((ns,ip,op))    # 1 is for out 
    inout[ns][0].append((cs,ip,op))    # 0 is for in

count = {}

for key,value in inout.items():
    count[key] = (len(value[0]),len(value[1]))
    for item_in in value[0]:
        for item_out in value[1]:
            inp = item_in[1] + item_out[1] 
            op = item_in[2] + item_out[2]
            cs = item_in[0]
            ns = item_out[0]    
total = 0
for key,value in count.items():
    total += value[0]*value[1]

filewrite.write(".p "+str(total)+'\n')
#print(namefile)
for key,value in inout.items():
    count[key] = (len(value[0]),len(value[1]))
    for item_in in value[0]:
        for item_out in value[1]:
            inp = item_in[1] + item_out[1] 
            op = item_in[2] + item_out[2]
            cs = item_in[0]
            ns = item_out[0]    
       	    filewrite.write(inp+" "+str(cs)+" "+str(ns)+" "+op+"\n") 
