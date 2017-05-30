import csv

with open("/Users/finvermehr/Downloads/train.csv", "rb") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",", quotechar='|')
    for column in spamreader:
        print (column)
