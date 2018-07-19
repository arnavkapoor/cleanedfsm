`masterscript.sh` runs everything in order.

`consolidated.py` takes 3 parameters: 
  1. cpu raw results
  2. gpu raw results
  3. 0 or 1 (0 is for minimum, 1 is for median values across experiment runs)
It generates two csv files one for the cpu and the other for the gpu.

`mergecsv.py` takes the csv files created previously and generates a consolidated file called `mergednetwork`.
`splitcsv.py` takes the path to which to save the data. It reads the `mergednetwork` file and splits the data for each benchmark in individual files.
