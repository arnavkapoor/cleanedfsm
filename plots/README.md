The scripts in `data-scripts` generate the csv files from the raw data.

`master-script.sh` inside `data-scripts` takes 4 parameters:
  1. the cpu raw result  
  2. the gpu raw result. 
  3. 0 or 1 (0 is for minimum values and 1 is for median values across all runs)
  4. the path to where to save the generated csv; 
     the path should have the same directory structure as the `data-generated` folder.

The scripts in `plotting-scripts` use the generated csvs. They assume the same directory structure as the one in `data-generated`.
