#downloading the current data files
import os
from urllib.request import urlopen

csv = ['GOOG.csv', 'IBM.csv', 'MSFT.csv']

url = ['https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1587042293&period2=1618578293&interval=1d&events=history&includeAdjustedClose=true',
'https://query1.finance.yahoo.com/v7/finance/download/IBM?period1=1587042293&period2=1618578293&interval=1d&events=history&includeAdjustedClose=true',
'https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=1587042293&period2=1618578293&interval=1d&events=history&includeAdjustedClose=true'
]
for i, j in zip(csv, url):
    local_path = os.path.join('data', i)
    with urlopen(j) as file, open(local_path, 'wb') as f:
        f.write(file.read())

#file operations
import csv

filenameG = open('data/GOOG.csv', 'r')
fileG = csv.DictReader(filenameG)

#creating empty lists
Date = []
Open = []
High = []
Low = []
Close = []
AdjClose = []
Volume = []

#iterating over each row and append values to empty list
for col in fileG:
    Date.append(col['Date'])
    Open.append(col['Open'])
    High.append(col['High'])
    Low.append(col['Low'])
    Close.append(col['Close'])
    AdjClose.append(col['Adj Close'])
    Volume.append(col['Volume'])

#converting the strings into integers (still without any digits -> change this)
OpenI = []
for element in Open:
    OpenI.append(float(element))

CloseI = []
for element in Close:
    CloseI.append(float(element))

#calculation of the changes
Change = []
for i in range(len(OpenI)):
    Change.append((CloseI[i]-OpenI[i])/OpenI[i])

#printing lists
print('GOOGLE')
print('Date:', Date)
print('Open:', OpenI)
print('High:', High)
print('Low:', Low)
print('Close:', CloseI)
print('AdjClose:', AdjClose)
print('Volume:', Volume)
print('Change:', Change)
Header = ["Date", "Open", "High", "Low", "Close", "AdjClose", "Volume", "Change"]

#making a new file out of it
rows = zip(Date, OpenI, High, Low, CloseI, AdjClose, Volume, Change)
file = open('data/new_GOOG.csv', 'w+', newline='')
with file:
    write = csv.writer(file)
    write.writerow(Header)
    write.writerows(rows)

#next file
filenameI = open('data/IBM.csv', 'r')
fileI = csv.DictReader(filenameI)

#creating empty lists
Date = []
Open = []
High = []
Low = []
Close = []
AdjClose = []
Volume = []

#iterating over each row and append values to empty list
for col in fileI:
    Date.append(col['Date'])
    Open.append(col['Open'])
    High.append(col['High'])
    Low.append(col['Low'])
    Close.append(col['Close'])
    AdjClose.append(col['Adj Close'])
    Volume.append(col['Volume'])

#converting the strings into integers (still without any digits -> change this)
OpenI = []
for element in Open:
    OpenI.append(float(element))

CloseI = []
for element in Close:
    CloseI.append(float(element))

#calculation of the changes
Change = []
for i in range(len(OpenI)):
    Change.append((CloseI[i]-OpenI[i])/OpenI[i])

#printing lists
print('IBM')
print('Date:', Date)
print('Open:', OpenI)
print('High:', High)
print('Low:', Low)
print('Close:', CloseI)
print('AdjClose:', AdjClose)
print('Volume:', Volume)
print('Change:', Change)
Header = ["Date", "Open", "High", "Low", "Close", "AdjClose", "Volume", "Change"]

#making a file out of it
rows = zip(Date, OpenI, High, Low, CloseI, AdjClose, Volume, Change)
file = open('data/new_IBM.csv', 'w+', newline='')
with file:
    write = csv.writer(file)
    write.writerow(Header)
    write.writerows(rows)

#next file
filenameM = open('data/MSFT.csv', 'r')
fileM = csv.DictReader(filenameM)

#creating empty lists
Date = []
Open = []
High = []
Low = []
Close = []
AdjClose = []
Volume = []

#iterating over each row and append values to empty list
for col in fileM:
    Date.append(col['Date'])
    Open.append(col['Open'])
    High.append(col['High'])
    Low.append(col['Low'])
    Close.append(col['Close'])
    AdjClose.append(col['Adj Close'])
    Volume.append(col['Volume'])

#converting the strings into integers (still without any digits -> change this)
OpenI = []
for element in Open:
    OpenI.append(float(element))

CloseI = []
for element in Close:
    CloseI.append(float(element))

#calculation of the changes
Change = []
for i in range(len(OpenI)):
    Change.append((CloseI[i]-OpenI[i])/OpenI[i])

#printing lists
print('MSFT')
print('Date:', Date)
print('Open:', OpenI)
print('High:', High)
print('Low:', Low)
print('Close:', CloseI)
print('AdjClose:', AdjClose)
print('Volume:', Volume)
print('Change:', Change)
Header = ["Date", "Open", "High", "Low", "Close", "AdjClose", "Volume", "Change"]

#making a file out of it
rows = zip(Date, OpenI, High, Low, CloseI, AdjClose, Volume, Change)
file = open('data/new_MSFT.csv', 'w+', newline='')
with file:
    write = csv.writer(file)
    write.writerow(Header)
    write.writerows(rows)