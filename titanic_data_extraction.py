import csv

with open("/Users/finvermehr/Downloads/train.csv", "rb") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",", quotechar='|')
    dic = dict()
    for column in spamreader:
        local_dic = {"Survived": column[1]}


#        local_dic = {"Survived": column[1], "Pclass": column[2], "Name": (column[3] + column[4]), "Sex": column[5], "Age": column[6], "SibSp": column[7], "Parch": column[8], "Ticket": column[9], "Fare": column[10], "Cabin": column[11], "Embarked": column[12]}
#        dic[column[0]] = local_dic

# print(dic['1']["Name"])
