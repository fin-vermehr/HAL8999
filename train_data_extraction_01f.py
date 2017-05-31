
import pandas as pd
from io import StringIO
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('/Users/finvermehr/Documents/GitHub/HAL8999/train.csv')

df['Cabin'] = df["Cabin"].fillna(0)
df['Embarked'] = df["Embarked"].fillna("Q")

cols_to_transform = ['Sex', 'Embarked']
df_with_dummies = pd.get_dummies(df, columns=cols_to_transform)
print(df_with_dummies)
