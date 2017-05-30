import csv

with open("/Users/finvermehr/Downloads/train.csv", "rb") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",", quotechar='|')
    dic = dict()
    for column in spamreader:
        if column[0] == "PassengerId":
            pass
        else:
            survived = column[1]
            pclass = column[2]
            name = (column[3] + column[4]).replace('"', "")
            sex = column[5]
            age = column[6]
            sibsp = int(column[7])
            parch = int(column[8])
            ticket = column[9]
            fare = column[10]
            cabin = column[11]
            embarked = column[12]

            local_dic = {"Survived": survived, "Pclass": pclass, "Name": name,
                         "Sex": sex, "Age": age, "SibSp": sibsp, "Parch": parch,
                         "Ticket": ticket, "Fare": fare, "Cabin": cabin,
                         "Embarked": embarked}

            dic[column[0]] = local_dic
    print(dic["344"])
