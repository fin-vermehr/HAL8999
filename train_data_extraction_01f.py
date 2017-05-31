
import pandas as pd
from io import StringIO
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder
"""
with open("/Users/finvermehr/Downloads/train.csv", "r") as csvfile:
    csv_rows = csv.reader(csvfile, delimiter=',', quotechar='|')
    data_dict = dict()

    for row in csv_rows:
        if row[0] == "PassengerId":
            pass
        else:
            survived = int(row[1])
            pclass = int(row[2])
            name = (row[3] + row[4]).replace('"', "")
            if row[5].strip() == "male":
                sex = 1  # if male then 1
            else:
                sex = 0  # if female then 0
            if not row[6]:
                age = 29.0  # will be replaced by Bindi
            else:
                age = float(row[6])
            sibsp = int(row[7])
            parch = int(row[8])
            ticket = row[9]
            fare = float(row[10])
            if row[11]:
                cabin = 1  # If they have a cabin then 1
            else:
                cabin = 0  # if they do not have a cabin then 0
            embarked = row[12]

            local_dic = {"Survived": survived, "Pclass": pclass, "Name": name,
                         "Sex": sex, "Age": age, "SibSp": sibsp, "Parch": parch,
                         "Ticket": ticket, "Fare": fare, "Cabin": cabin,
                         "Embarked": embarked}

            data_dict[row[0]] = local_dic

print(data_dict["2"])
"""
df = pd.read_csv('/Users/finvermehr/Documents/GitHub/HAL8999/train.csv')

df['Cabin'] = df["Cabin"].fillna(0)
df['Embarked'] = df["Embarked"].fillna("Q")

cols_to_transform = ['Sex', 'Embarked']
df_with_dummies = pd.get_dummies(df, columns=cols_to_transform)
print(df_with_dummies)
#imr = Imputer(missing_values='Nan', strategy='mean', axis=0)
#imr = imr.fit(df)
#imputed_data = imr.transform(df.values)
#print(imputed_data)
