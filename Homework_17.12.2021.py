import os
import csv
from urllib.request import urlopen

#url = 'https://query1.finance.yahoo.com/v7/finance/download/IBM?period1=1607354575&period2=1638890575&interval=1d&events=history&includeAdjustedClose=true'

#local_path = os.path.join('data', 'GOOG.csv')
#with urlopen(url) as file, open(local_path, 'wb') as f:
 #   f.write(file.read())

# repeat this for every file to download the CSV files. As I did it before I put the commands as comments to not repeat it every time I run the program.

def get_stocks():
    GOOG = 'data/GOOG.csv'
    IBM = 'data/IBM.csv'
    MSFT = 'data/MSFT.csv'
    GOOG = []
    IBM = []
    MSFT = []
    with open('GOOG') as old_GOOG:
        for rowsG in old_GOOG:
            rowsG.append(rowsG.strip())
    return rowsG
    with open('IBM') as old_IBM:
        for rowsI in old_IBM:
            rowsI.append(rowsI.strip())
    return rowsI
    with open('MSFT') as old_MSFT:
        for rowsM in old_MSFT:
            rowsM.append(rowsM.strip())
    return rowsM
    with open('GOOG', newline='') as old_GOOG:
        writer = csv.writer(old_GOOG, quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow((['Close']-['Open'])/['Open'])
        for i, row in enumerate('GOOG'):
            if i != 0:
                row.append('changes in a day')
                writer.writerow(row)
        csv.saveas(new_GOOG)
        close(old_GOOG and new_GOOG)
#https://docs.python.org/3/library/csv.html

    #directory = os.path.join('c:\\', 'C:/Users/schus/PycharmProjects/pythonProject1/data')
    #for root, dirs, files in os.walk(directory):
      #  for file in files:
       ##     if file.endswith(".csv"):
         #       f = open(file, 'r')
          #      print(f)
           #     f.colse()
#vielleicht mit den festen Namen und einer Datei anfangen um wenigstens einen Anfang zu haben