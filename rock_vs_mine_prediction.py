# -*- coding: utf-8 -*-
"""Rock VS mine prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oGfeHWWmYGdKMOdgmLxhxXopAKQpdxb8
"""



"""Importing the dependencies"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data Collection and Data Processing"""

#loading the data set to a pandas dataframe
sonar_data = pd.read_csv('/content/sonar data.csv', header=None)

sonar_data.head()
#first 5 rows and 61 columns

#number of rows and columns in the entire dataset
#60 features for a rock/mine and the 61st shows IF its a rock or mine
sonar_data.shape

sonar_data.describe()
#the values for each rock/mine
#better statistical understanding of data

sonar_data[60].value_counts()
#why 60? the value of if it is a rock or mine i given in the 60th column
#almost equal number of examples for both categories make the analysis better.
#more the data, more accurate the model is

"""M - mine

R -  rock
"""

sonar_data.groupby(60).mean()

#separating data and labels (since this is supervised learning)
X = sonar_data.drop(columns=60, axis=1)
Y = sonar_data[60]

print(X)
print(Y)

"""Training and Test data

"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1)
#10 percent of data is test data
#stratify - based on number of rocks and mine
#random_state - the way split happens

print(X.shape, X_train.shape, X_test.shape)

print(X_train)
print (Y_train)

"""Model Training - logistic regression"""

model = LogisticRegression()

#training logistic regression model with training data
model.fit(X_train, Y_train)

"""Model evaluation"""

#accuracy on the training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on training data: ', training_data_accuracy)

#accuracy on the test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy on test data: ', test_data_accuracy)

"""Making a predictive system"""

input_data = (0.0346,0.0509,0.0079,0.0243,0.0432,0.0735,0.0938,0.1134,0.1228,0.1508,0.1809,0.2390,0.2947,0.2866,0.4010,0.5325,0.5486,0.5823,0.6041,0.6749,0.7084,0.7890,0.9284,0.9781,0.9738,1.0000,0.9702,0.9956,0.8235,0.6020,0.5342,0.4867,0.3526,0.1566,0.0946,0.1613,0.2824,0.3390,0.3019,0.2945,0.2978,0.2676,0.2055,0.2069,0.1625,0.1216,0.1013,0.0744,0.0386,0.0050,0.0146,0.0040,0.0122,0.0107,0.0112,0.0102,0.0052,0.0024,0.0079,0.0031)
#changing the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the numpy array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 'R'):
  print('The object is a rock')
else:
  print('It is a mine')

