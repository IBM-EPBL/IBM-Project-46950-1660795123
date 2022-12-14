# -*- coding: utf-8 -*-
"""Assignment-4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hq5vL88W-nkoZHYJ3QNORuBN8YWso0Te

Assignment 4

Team id - IBM-Project-PNT2022TMID31735
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

d=pd.read_csv("Mall_Customers.csv")
d=d.rename(columns = {'Annual Income (k$)' : 'Annual_Income','Spending Score (1-100)' : 'Spending_Score'})
d.head()

d.shape

d.info()

"""Performing Various Visualisations

Univariate Analysis
"""

sns.barplot(d.Age)

"""Bivariate Analysis"""

sns.boxplot(y=d.Gender,x=d.Age)

"""Multivariate Analysis"""

sns.pairplot(d)

"""Performing descriptive statistics on the dataset."""

d.describe(include='all')

"""Checking for Missing values"""

d.isnull().sum()

sns.boxplot(d['Annual_Income'])

q1 = d.Annual_Income.quantile(0.25)
q2 = d.Annual_Income.quantile(0.75)
IQR = q2 - q1
print(IQR)

d=d[~((d.Annual_Income<(q1-1.5*IQR))|(d.Annual_Income>(q2+1.5*IQR)))]
d

sns.boxplot(d['Annual_Income'])

"""Checking for Categorical columns and perform Encoding"""

d.head()

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
d.Gender = le.fit_transform(d.Gender)

d.head()

"""Scaling the data"""

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(d)
data_scaled[0:5]

"""Performing any of the clustering algorithms"""

from sklearn.cluster import KMeans
km = KMeans()
res = km.fit_predict(data_scaled)
res

data1 = pd.DataFrame(data_scaled, columns = d.columns)
data1.drop('CustomerID',axis=1,inplace=True)
data1.head()

data1['kclus']  = pd.Series(res)
data1.head()

data1['kclus'].unique()

data1['kclus'].value_counts()

import matplotlib.pyplot as plt
fig,ax = plt.subplots(figsize=(15,8))
sns.scatterplot(x=data1['Annual_Income'],
                y=data1['Spending_Score'],
                hue=data1['kclus'],
                palette='PuBuGn')
plt.show()

ind = data1.iloc[:,0:4]
ind.head()

dep = data1.iloc[:,4:]
dep.head()

"""Splitting dataset into train and test data"""

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(ind,dep,test_size=0.3,random_state=1)
x_train.head()

x_test.head()

y_train.head()

y_test.head()

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train,y_train)

pred_test = lr.predict(x_test)
pred_test[0:5]

"""Measuring the performance using metrics"""

from sklearn.metrics import mean_squared_error,mean_absolute_error
from sklearn.metrics import accuracy_score
mse = mean_squared_error(pred_test,y_test)
print("The Mean squared error is: ", mse)
rmse = np.sqrt(mse)
print("The Root mean squared error is: ", rmse)
mae = mean_absolute_error(pred_test,y_test)
print("The Mean absolute error is: ", mae)
acc = lr.score(x_test,y_test)
print("The accuracy is: ", acc)