import os
from urllib.request import urlopen

url = 'https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=1607083050&period2=1638619050&interval=1d&events=history&includeAdjustedClose=true'

local_path = os.path.join('data', 'MSFT.csv')
with urlopen(url) as file, open(local_path, 'wb') as f:
    f.write(file.read())

#repeat this for every file

if __name__ == '__main__':
