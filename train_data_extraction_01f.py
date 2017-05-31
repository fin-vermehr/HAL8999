
import pandas as pd
from io import StringIO
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('/Users/finvermehr/Documents/GitHub/HAL8999/train.csv')

df['Cabin'] = df["Cabin"].fillna(0)
df['Embarked'] = df["Embarked"].fillna("Q")

df.loc[df['Name'].str.contains('Dr.'), 'Title'] = "Dr."
df.loc[df['Name'].str.contains('Mr.'), 'Title'] = "Mr."
df.loc[df['Name'].str.contains('Mrs.'), 'Title'] = "Mrs."
df.loc[df['Name'].str.contains('Miss.'), 'Title'] = "Miss."
df.loc[df['Name'].str.contains('Master.'), 'Title'] = "Master."
df.loc[df['Name'].str.contains('Rev.'), 'Title'] = "Rev."

cols_to_transform = ['Sex', 'Embarked', "Title"]
df_with_dummies = pd.get_dummies(df, columns=cols_to_transform)
print(df_with_dummies)
df_with_dummies.to_csv("/Users/finvermehr/Documents/GitHub/HAL8999/preprocessed_data.csv", sep='\t', encoding='utf-8')
