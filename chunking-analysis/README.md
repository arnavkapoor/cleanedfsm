`python consolidatedanalysis.py 'path/to/chunked/results'`

`consolidatedanalysis.py` saves a file called `all.csv` that contains data for all possible chunk sizes.

`python min_of_all.py`

`min_of_all.py` picks the best theoretical and actual values from `all.csv` and saves them in `overheadtransfer.csv`.
