import os
import csv
from urllib.request import urlopen

# url = 'https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=1607083050&period2=1638619050&interval=1d&events=history&includeAdjustedClose=true'

# local_path = os.path.join('data', 'MSFT.csv')
# with urlopen(url) as file, open(local_path, 'wb') as f:
# f.write(file.read())

# repeat this for every file to download the CSV files. As I did it before I put the commands as comments to not repeat it every time I run the program.

if __name__ == '__main__':
    directory = os.path.join('c:\\', 'C:/Users/schus/PycharmProjects/pythonProject1/data')
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                f = open(file, 'r')
                print(f)
                f.colse()
#vielleicht mit den festen Namen und einer Datei anfangen um wenigstens einen Anfang zu haben