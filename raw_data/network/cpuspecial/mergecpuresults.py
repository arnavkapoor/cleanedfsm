import sys,os,csv
import math
import numpy as np
import pandas as pd
import itertools


def isfloat(value):
  try:
    float(value)
    return True
  except:
    return False

path = sys.argv[1]     # directory containing cpu results ../denseresults/sorted  
cputimes = {}

for folder, sub_folders, files in os.walk(path):
    flag = 0;
    splitfolder = folder.split('/')
    for elements in splitfolder:
        if(elements == "with-offsets" or elements == "gputestresultsnetwork"):
            flag = 1;
            break;
    
    if(flag == 0):
        for special_file in files:
            if special_file not in cputimes.keys():
                cputimes[special_file] = []
            file_path = os.path.join(folder, special_file)
            with open(file_path, 'r+') as read_file:
                for lines in read_file:
                    lines = lines.strip()
                    if(isfloat(lines)):
                        cputimes[special_file].append(float(lines));

# for key, value in cputimes.items():
#     print(key,len(value))   ( checking results)

finalresults = {}

for key, value in cputimes.items():
    value.sort()

filenames = []

for key, value in cputimes.items():
    keys=key.split('_')
    filename = keys[2].split('.')[0]+".csv"
    if(filename not in filenames):
        file = csv.writer(open(filename,'w'))
        filenames.append(filename)
    else:
        file = csv.writer(open(filename,'a'))
    file.writerow([keys[2].split('.')[0]+".test",keys[0],keys[1],value[0]])  #value[0] takes the minimum   
    
for elements in filenames:
    data = csv.reader(open(elements))
    sortedlist = sorted(data,key=lambda row: (float(row[1]),float(row[2])), reverse=True)    # 0 specifies according to first column we want to sort
    file = csv.writer(open(elements,'w'))
    file.writerow(['FSM', 'Testcases', 'Cores' ,'Total CPU' ])        
    for row in sortedlist:
        file.writerow(row)
