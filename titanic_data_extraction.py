#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import csv
from sklearn import svm

with open("/Users/finvermehr/Downloads/train.csv", "r") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",", quotechar='|')
    dic = dict()
    for row in spamreader:
        if row[0] == "PassengerId":
            pass
        else:
            survived = row[1]
            pclass = row[2]
            name = (row[3] + row[4]).replace('"', "")
            sex = row[5]
            age = row[6]
            sibsp = int(row[7])
            parch = int(row[8])
            ticket = row[9]
            fare = row[10]
            cabin = row[11]
            embarked = row[12]

            local_dic = {"Survived": survived, "Pclass": pclass, "Name": name,
                         "Sex": sex, "Age": age, "SibSp": sibsp, "Parch": parch,
                         "Ticket": ticket, "Fare": fare, "Cabin": cabin,
                         "Embarked": embarked}

            dic[row[0]] = local_dic
sum_, count = 0, 0
for x in dic:
    if dic[x]["Age"]:
        count += 1
        sum_ += float(dic[x]["Age"])
for x in dic:
    if not dic[x]["Age"]:
        dic[x]["Age"] = float(sum_ / count)
    else:
        dic[x]["Age"] = float(dic[x]["Age"])
print(dic["6"])
