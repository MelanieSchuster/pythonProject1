import os
from fileinput import filename
from urllib.request import urlopen

#url = 'https://query1.finance.yahoo.com/v7/finance/download/IBM?period1=1607354575&period2=1638890575&interval=1d&events=history&includeAdjustedClose=true'

#local_path = os.path.join('data', 'GOOG.csv')
#with urlopen(url) as file, open(local_path, 'wb') as f:
 #   f.write(file.read())

# repeat this for every file to download the CSV files. As I did it before I put the commands as comments to not repeat it every time I run the program.

#importing the module
import csv

#open the file in read mode
directory = 'C:/Users/schus/PycharmProjects/pythonProject1/data'
data = os.listdir(directory)

header = []
data = []

for file in directory:
    if file.lower().endswith('.csv'):
        with open(f'{directory}/{file}', 'r') as csv_file:
            file = csv.DictReader(csv_file)
            header = next(file)
            data.extend([row for row in file])


with open('data/new_GOOG.csv', 'w', newline='') as solution:
    write = csv.writer(solution)
    write.writerow(header)
    write.writerows(data)

GOOG = 'data/GOOG.csv'
IBM = 'data/IBM.csv'
MSFT = 'data/MSFT.csv'


