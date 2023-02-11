import csv
import re

filein = open('./FIPS_StateCounty_Code.csv', 'r')
fileout = open('FIPS_StateCounty_Code_Formatted.csv', 'w', newline='')
lines = filein.readlines()
w = csv.writer(fileout)
w.writerow(['FIPS State', 'FIPS County', 'County', 'State'])
for i in lines:
    if i and i[0].isnumeric():
        arr = re.split('[ ]{2,}', i)
        arr[-1] = arr[-1][:2]
        if arr[0] == '72':
            break
        w.writerow(arr[:4])
        w.writerow(arr[4:])