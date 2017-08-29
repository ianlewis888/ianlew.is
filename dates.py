from lxml import html
import requests
import csv

dates = []

with open('/Users/ianlewis/Documents/GitHub/ianlew.is/dates.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        row[1] = row[1].replace("20","19",1)
        #print(row)
        dates.append(row)

print(dates)

with open('/Users/ianlewis/Documents/GitHub/ianlew.is/dates output.csv','wb') as csvfile:
    writeCSV = csv.writer(csvfile, delimiter=',')
    for row in dates:
        writeCSV.writerow(row)
