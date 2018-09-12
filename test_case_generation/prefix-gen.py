import sys
import itertools
import os
from collections import deque
fsm = []

with open(sys.argv[1], 'r') as myfile1: # the fsm file
    fsmdata=myfile1.readlines()

for i in range(0,len(fsmdata)):
    fsm.append(fsmdata[i].strip().split())

namefile=(sys.argv[1].rsplit('/',1)[1])
outputdir=sys.argv[2]

filewrite= open(os.path.join(outputdir+"/prefix_list",namefile),"w")
#filewrite1= open(os.path.join('/home/arnav/fsm/tests/opensrcexpanded',namefile),"w")

# print(namefile)
userinput = []
currstate = []
nextstate = []
useroutput = []

visited = []
valid_digits = []
wildcard_compare = []

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
    currstate[i] = int(currstate[i],base=base)    

for i in range(0,len(nextstate)):
    nextstate[i] = int(nextstate[i],base=base)

for i in range(0,2):
    valid_digits.append(i) # list containing (0,1,2,...b-1)

for i in itertools.product(valid_digits,repeat=inputlen):
    wildcard_compare.append(i)

x=len(userinput)



# def compare(comp,s): 
#     wild_present = False
#     valid = True
   
#     for i in range(0,len(comp)):
#         if(comp[i] == "-"):
#             wild_present = True

#         if(comp[i] != str(s[i]) and comp[i] != "-" ):
#             valid = False
    
#     if(wild_present == True and valid == True):
#         return True

#     return False     

for i in range(x-1,-1,-1):
    
    inp = userinput[i]
    op = useroutput[i]
    cs = currstate[i]
    ns = nextstate[i]
    vs = visited[i]

    # if "-" in inp:
    #     userinput.pop(i)
    #     useroutput.pop(i)
    #     currstate.pop(i)
    #     nextstate.pop(i)
    #     visited.pop(i)
    #     for s in range(0,len(wildcard_compare)):
    #         if(compare(inp,wildcard_compare[s])):
    #             x = ''.join(map(str,wildcard_compare[s]))
    #             userinput.append(x)
    #             useroutput.append(op)
    #             currstate.append(cs)
    #             nextstate.append(ns)
    #             visited.append(vs)


# filewrite1.write(".i "+str(inputlen) + "\n")
# filewrite1.write(".o "+str(outputlen)+ "\n")
# filewrite1.write(".s 2"+ "\n")
# filewrite1.write(".p "+str(len(userinput))+ "\n")
# filewrite1.write(".b 10" + "\n")

# print(len(userinput),len(currstate),len(nextstate),len(useroutput))


q = deque()
q.append(currstate[0])

dequed = {}

testcases = []
visited = {}

visited[currstate[0]] =  " "

while(q):
    ele = q.popleft()
    if ele in dequed:
        continue
    prefix = visited[ele]    
    dequed[ele] = 1  
    for i in range(0,len(userinput)):
        s1 = currstate[i]
        s2 = nextstate[i]
        if(s1 == ele):
            if s2 not in visited:    
                visited[s2] = prefix + userinput[i]
                testcases.append(prefix+userinput[i])
            else:
                testcases.append(prefix+userinput[i])        
            if(s2 not in dequed):       
                q.append(s2)

for key in visited:
    filewrite.write(str(key) +" "+ visited[key]+"\n")
