import csv

rowscpu = []
rowsgpu = []

with open("cpuresultsnetwork.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rowscpu.append(row)

with open("gpuresultsnetwork.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rowsgpu.append(row)

file = csv.writer(open("mergednetwork.csv",'w'))
file.writerow(['FSM', 'Testcases', 'Cores' ,'Total CPU' , 'Execution GPU', 'Total GPU'])		

superlist = []

for elements in rowscpu:
	superlist.append(elements)

for gpuele in rowsgpu:
	fsm = gpuele[0]
	tests = gpuele[1]
	for lists in superlist:
		if lists[0] == fsm and lists[1] == tests and len(lists) == 4:	
			lists.append(gpuele[2]) 
			lists.append(gpuele[3])


superlist.sort(key=lambda x:(x[0],-int(x[1]),-int(x[2])))
for lists in superlist:
	file.writerow(lists)

file.writerow(['blank','blank','blank','blank','blank','blank'])	
