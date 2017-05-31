import pandas as pd
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn import datasets
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
import csv
from sklearn import svm
from mpl_toolkits.mplot3d import Axes3D

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
            if row[5].strip() == "male":
                sex = 0
            else:
                sex = 1
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
age_list = list()
survived_list = list()
for x in dic:
    if dic[x]["Age"]:
        count += 1
        sum_ += float(dic[x]["Age"])
for x in dic:
    if not dic[x]["Age"]:
        dic[x]["Age"] = float(sum_ / count)
    else:
        dic[x]["Age"] = float(dic[x]["Age"])

    age_list.append(dic[x]["Age"])

target = list()
array_list = list()

for x in dic:
    sample = [int(dic[x]["Pclass"]), int(dic[x]["Age"]), int(dic[x]["Parch"]),
              int(dic[x]["SibSp"]), int(dic[x]["Sex"])]
    target.append(int(dic[x]["Survived"]))
    array_list.append(sample)

#df = pd.read_csv('https://archive.ics.uci.edu/ml/''machine-learning-databases/iris/iris.data', header=None)
#print(df.tail())
#y = df.iloc[0:100, 4].values
#y = np.where(y == 'Iris-setosa', -1, 1)
#print(type(y))

# X = np.array(array_list).reshape((891, 2))
# y = target
# print(type(y))
#print(len(target))
#print(len(array_list))
X = array_list
y = target
clf = svm.SVC()
clf.fit(X, y)
print(clf.predict([[1, 20, 1, 2, 1]]))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
index = 0

for i in target:
    if i == 0:
        Pclass = X[index][0]
        Age = X[index][1]
        Parch = X[index][-1]

        ax.scatter(Pclass, Age, Parch, c='r', marker='o')

    else:
        Pclass = X[index][0]
        Age = X[index][1]
        Parch = X[index][-1]

        ax.scatter(Pclass, Age, Parch, c='b', marker='x')
    index += 1
ax.set_xlabel('Class')
ax.set_ylabel('Age')
ax.set_zlabel('Sex')

print(X)
print(y)


plt.show()
