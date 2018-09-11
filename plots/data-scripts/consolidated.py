import os,csv,sys
path = sys.argv[1] #directory having cpuresults
path2 = sys.argv[2] #directory having gpuresults
value_taken = sys.argv[3]




file = csv.writer(open('cpuresultsnetwork.csv', 'w'))

for folder, sub_folders, files in os.walk(path):
    for special_file in files:
        file_path = os.path.join(folder, special_file)
        with open(file_path, 'r+') as read_file:
            count = 0
            time = []
            for line in read_file:
                try:
                    float(line)
                    count+=1
                    time.append(float(line))
                except:
                   pass    
            special_file=special_file.split('_')        
            time.sort()
            if(value_taken == "0"):
                file.writerow([special_file[2],special_file[0],special_file[1],time[0]])
            else:
                file.writerow([special_file[2],special_file[0],special_file[1],time[count//2+1]])
                
file2 = csv.writer(open('gpuresultsnetwork.csv', 'w'))

for folder, sub_folders, files in os.walk(path2):
    for special_file in files:
        file_path = os.path.join(folder, special_file)
        print(special_file)
        with open(file_path, 'r+') as read_file:
            count = 0
            totaltime = []
            exectime = []
            for line in read_file:
                line=line.split()
                try:
                    float(line[0])
                    float(line[1])
                    float(line[2])
                    float(line[3])
                    count+=1
                    totaltime.append(float(line[3]))
                    exectime.append(float(line[2]))
                except:
                    pass   
            special_file=special_file.split('_')  
            totaltime.sort()
            exectime.sort()
            if(value_taken == "0"):
                file2.writerow([special_file[1],special_file[0],exectime[0],totaltime[0]])
            else:    
                file2.writerow([special_file[1],special_file[0],exectime[count//2+1],totaltime[count//2+1]])
