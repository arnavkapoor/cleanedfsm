import os
import re
import sys
path = sys.argv[1]
with open(path, 'r+') as fsmfile:
    alllines=fsmfile.readlines()
    length=[]
    for lines in alllines:
        if len(lines.split(" ")) == 2: 
            string = lines.split(" ")[1]
            totallen = len(string)
            string = string.strip()
            escaped = ['a','b','t','n','v','f','r','\\']
            numbers = [ '0','1','2','3','4','5','6','7']
            i = 0
            while(i<len(string)):
                if(string[i] == '\\'):
                    try:
                        if(string[i+1] in escaped):
                            totallen = totallen - 1
                            i=i+1
                        else:
                            if(string[i+1] in numbers and string[i+2] in numbers and string[i+3] in numbers):
                                i=i+3
                                totallen = totallen - 3 
                    except:
                        pass 
                i=i+1        
            length.append(totallen)            
    length.sort()
    print(length[len(length)-1])
