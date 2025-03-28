# -*- coding: utf-8 -*-
"""Titanic Survival .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZttuhwEFaWXMZ17rFeKSeRl3ByotCmiA
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

titanic_data = pd.read_csv("/content/train.csv")

titanic_data.head()

titanic_data.shape

titanic_data.info()

titanic_data.isnull().sum()

titanic_data = titanic_data.drop(columns='Cabin', axis=1)

titanic_data["Age"].fillna(titanic_data['Age'].mean(),inplace=True)

print(titanic_data['Embarked'].mode())

print(titanic_data['Embarked'].mode()[0])

titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode()[0], inplace=True)

titanic_data.isnull().sum()

titanic_data.describe()

titanic_data['Survived'].value_counts()

sns.set()

sns.countplot(x='Survived', data=titanic_data)

titanic_data['Sex'].value_counts()

sns.countplot(x='Sex', data=titanic_data)

sns.countplot(x='Sex', hue='Survived', data=titanic_data)

sns.countplot(x='Pclass', data=titanic_data)

sns.countplot(x='Pclass', hue='Survived', data=titanic_data)

titanic_data['Sex'].value_counts()

titanic_data['Embarked'].value_counts()

titanic_data.replace({'Sex':{'male':0,'female':1}, 'Embarked':{'S':0,'C':1,'Q':2}}, inplace=True)

titanic_data.head()

x = titanic_data.drop(columns = ['PassengerId','Name','Ticket','Survived'],axis=1)
y = titanic_data['Survived']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=2)

print(x.shape, x_train.shape, x_test.shape)

model = LogisticRegression()

model.fit(x_train, y_train)

x_train_prediction = model.predict(x_train)

print(x_train_prediction)

training_data_accuracy = accuracy_score(y_train, x_train_prediction)
print('Accuracy score of training data : ', training_data_accuracy)

x_test_prediction = model.predict(x_test)

print(x_test_prediction)

test_data_accuracy = accuracy_score(y_test, x_test_prediction)
print('Accuracy score of test data : ', test_data_accuracy)