# Calulate activity K-40 in KCl, Lu-176 in Lu2O3

Steps to run:

Install requirements:

`pip install -r ./requirements.txt`

run Jupiter books

If you have error with fetching nudat3 file from nndc, change this code in file `venv/Lib/site-packages/becquerel/tools/nndc.py`: 

443 line: `if not resp.ok or resp.status_code != 200:`