import csv
import pandas as pd

rowsall = []
df = pd.read_csv('./all.csv')



Fsm = (df['Fsm'].values.tolist())
totaltime = (df['totaltime'].values.tolist())
theoretical = (df['theoretical best'].values.tolist())

i=0
mini=1000
thmini=1000
filer = csv.writer(open("overheadtransfer.csv",'w'))
filer.writerow(["FSM","minimum total-time","minimum theoretical total-time"])	

while i<len(Fsm)-1:
	if Fsm[i] == Fsm[i+1]:
		mini=min(totaltime[i],mini)
		thmini=min(theoretical[i],thmini)
	else:
		filer.writerow([Fsm[i],mini,thmini])		
		mini=1000
		thmini=1000
	i=i+1

filer.writerow([Fsm[i],mini,thmini])	
