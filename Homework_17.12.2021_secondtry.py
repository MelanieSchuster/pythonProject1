import os
from urllib.request import urlopen

#url = 'https://query1.finance.yahoo.com/v7/finance/download/IBM?period1=1607354575&period2=1638890575&interval=1d&events=history&includeAdjustedClose=true'

#local_path = os.path.join('data', 'GOOG.csv')
#with urlopen(url) as file, open(local_path, 'wb') as f:
 #   f.write(file.read())

# repeat this for every file to download the CSV files. As I did it before I put the commands as comments to not repeat it every time I run the program.

import csv
import json

GOOG = 'data/GOOG.csv'
IBM = 'data/IBM.csv'
MSFT = 'data/MSFT.csv'

def csv_to_json(csv_path, headers) -> list:
    data = {}
    json_data = []
    with open(csv_path, encoding='uft-8') as file:
        reader = csv.DictReader(file)
        if headers:
            columns = next(reader)
        for row in reader:
            row_data = {}
            for i in range(len(row)):
                if headers:
                    row_key = columns[i].lower()
                else:
                    row_key = i
            row_data[row_key] = row[i]
        json_data.append(row_data)
    return json_data
    csv_path = 'data/GOOG.csv'
