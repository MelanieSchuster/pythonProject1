import os
from urllib.request import urlopen

#url = 'https://query1.finance.yahoo.com/v7/finance/download/IBM?period1=1607354575&period2=1638890575&interval=1d&events=history&includeAdjustedClose=true'

#local_path = os.path.join('data', 'GOOG.csv')
#with urlopen(url) as file, open(local_path, 'wb') as f:
 #   f.write(file.read())

# repeat this for every file to download the CSV files. As I did it before I put the commands as comments to not repeat it every time I run the program.

#importing the module
import csv

#open the file in read mode
filename = open('data/GOOG.csv', 'r')

#creating dictreader object
file = csv.DictReader(filename)

#creating empty lists
Date = []
Open = []
High = []
Low = []
Close = []
AdjClose = []
Volume = []

#iterating over each row and append values to empty list
for col in file:
    Date.append(col['Date'])
    Open.append(col['Open'])
    High.append(col['High'])
    Low.append(col['Low'])
    Close.append(col['Close'])
    AdjClose.append(col['Adj Close'])
    Volume.append(col['Volume'])

#printing lists
print('Date:', Date)
print('Open:', Open)
print('High:', High)
print('Low:', Low)
print('Close:', Close)
print('AdjClose:', AdjClose)
print('Volume:', Volume)

GOOG = 'data/GOOG.csv'
IBM = 'data/IBM.csv'
MSFT = 'data/MSFT.csv'


