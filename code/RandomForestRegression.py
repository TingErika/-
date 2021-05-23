#coding=utf-8
# @Author: chenyuanzhe
# @Time: 2021-04-10 16:11

import numpy as np
import pandas as pd
from sklearn import ensemble
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

dataset = pd.read_csv('all.csv')
x = dataset.iloc[1:,:2].values
y = dataset.iloc[1:, 2].values

#对国家特征进进行OneHot编码
labelencoder = LabelEncoder()
labelencoder.fit(["Canada","China","Iran","Iraq","Kuwait","Nigeria","Russia","Saudi Arabia","United Arab Emirates","United States"])
x[:,0] = labelencoder.fit_transform(x[:,0])
transformer = ColumnTransformer([("country",OneHotEncoder(),[0])], remainder='passthrough')
x= transformer.fit_transform(x).toarray()

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.9, test_size=0.1, random_state=0)
model_RandomForestRegressor = ensemble.RandomForestRegressor(n_estimators=20)
model_RandomForestRegressor.fit(x_train, y_train)

#预测
y_predict = model_RandomForestRegressor.predict(x_test)
print("y_test:",y_test)
print("y_predict:",y_predict)
rmse=np.sqrt(mean_squared_error(y_test,y_predict))
print("rmse:",rmse)
score=model_RandomForestRegressor.score(x_test,y_test)
print("score:",score)
plt.xlabel("Luminous (nanoWatts)")
plt.ylabel("Oil Production (Barrels)")
plt.scatter(x_train[:,-1],y_train,label='train')
plt.scatter(x_test[:,-1],y_test,label='test')
plt.scatter(x_test[:,-1],y_predict,label='predict')
plt.legend()
plt.show()

