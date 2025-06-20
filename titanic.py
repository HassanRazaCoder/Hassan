# -*- coding: utf-8 -*-
"""Titanic.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13k_H8TOPrkZpwGPtWt90_VjqLcj6y-28
"""

# Usually already installed in Colab, but just in case:
!pip install pandas numpy seaborn matplotlib scikit-learn

import pandas as pd
import seaborn as sns

# Load Titanic dataset
df = sns.load_dataset('titanic')
df.head()

df.shape
df.info()
df.describe()
df.isnull().sum()
df.nunique()

import seaborn as sns
import matplotlib.pyplot as plt

# Survival count
sns.countplot(x='survived', data=df)
plt.show()

# Survival by gender
sns.countplot(x='survived', hue='sex', data=df)
plt.show()

# Age distribution
sns.histplot(df['age'].dropna(), kde=True)
plt.show()

# Drop 'deck' due to too many missing values
df.drop(['deck'], axis=1, inplace=True)

# Fill 'age' with median
df['age'].fillna(df['age'].median(), inplace=True)

# Fill 'embarked' with mode
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)

df.isnull().sum()

# Convert 'sex' and 'embarked' using get_dummies
df = pd.get_dummies(df, columns=['sex', 'embarked'], drop_first=True)
df.head()

features = ['pclass', 'age', 'sibsp', 'parch', 'fare', 'sex_male', 'embarked_Q', 'embarked_S']
X = df[features]
y = df['survived']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()
rf.fit(X_train, y_train)
print("Random Forest Accuracy:", rf.score(X_test, y_test))

import joblib

joblib.dump(model, 'titanic_model.pkl')