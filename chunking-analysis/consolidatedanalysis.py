import os,csv,sys
from copy import deepcopy



def theoreticalmin(inp):
    time = 0
    
    time += inp[0][0]
    
    if(len(inp) > 1): 
        time += max(inp[1][0],inp[0][1])
    
    for i in range(0,len(inp)-2):
        transferin = inp[i+2][0]
        exectime = inp[i+1][1]
        transferback = inp[i][2]
        time += max(transferin,exectime,transferback)

    if(len(inp) > 1): 
        time += max(inp[len(inp)-1][1],inp[len(inp)-2][2])
        
    time += inp[len(inp)-1][2]
    
    if(len(inp)==1):
        time+=inp[0][1]

    return time  


path = sys.argv[1]
neededfiles = ['aim.test','battlefield2.test','counterstrike-source.test','dns.test','h323.test','halflife2-deathmatch.test','hotline.test','ntp.test','rtp.test','ssl.test','tsp.test','yahoo.test']
file = csv.writer(open('all.csv', 'w'))
file.writerow(['Fsm','totaltime','theoretical best','number of chunks','chunksize','total difference','differnece per chunk'])         
    
for folder, sub_folders, files in os.walk(path):
    for special_file in files:
        file_path = os.path.join(folder, special_file)
        special_file=special_file.split('_')
        
        with open(file_path, 'r+') as read_file:
            
            count = 0
            chunktime = []
            theoreticaltimes = []
            totaltime = []
            
            for line in read_file:
                line=line.split()
                #print(line)
                if(len(line) == 3):
                    try:
                        float(line[0])
                        float(line[1])
                        float(line[2])
                        chunktime.append([float(line[0]),float(line[1]),float(line[2])])
                    except:
                        pass
                if(len(line) == 4):
                    try:    
                        float(line[0])
                        float(line[1])
                        float(line[2])
                        float(line[3])
                        chunktime.append([float(line[0]),float(line[1]),float(line[2])])                        
                        totaltime.append(float(line[3]))
                    except:
                        pass
            
            idealtotaltime = []
            noofchunk=len(chunktime)//len(totaltime)
            
            for i in range(0,len(chunktime),noofchunk):
                newlist=chunktime[i:i+noofchunk]
                res=theoreticalmin(newlist)
                idealtotaltime.append(res)
            
            xy = zip(totaltime,idealtotaltime)
            xy=sorted(xy)
            xy=list(xy)
            realmedian = xy[50][0]
            theorymedian = xy[50][1]
            file.writerow([special_file[2],realmedian,theorymedian,noofchunk,special_file[1],(realmedian-theorymedian),((realmedian-theorymedian)/noofchunk)])    