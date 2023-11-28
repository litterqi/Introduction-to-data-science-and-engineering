import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import plotly.express as px #graphing
import missingno as msno #describe data
import os
from sklearn.feature_selection import SelectKBest
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv("/kaggle/input/nbaplayersdraft.csv")

df=df.dropna()

X = df[['rank']]
y_points = df['points_per_game']
y_minutes = df['average_minutes_played']

X_train, X_test, y_train_points, y_test_points = train_test_split(X, y_points, test_size=0.5, random_state=23)
X_train, X_test, y_train_minutes, y_test_minutes = train_test_split(X, y_minutes, test_size=0.5, random_state=23)

model_points = LinearRegression()
model_minutes = LinearRegression()

model_points.fit(X_train, y_train_points)
model_minutes.fit(X_train, y_train_minutes)

y_pred_points = model_points.predict(X_test)
y_pred_minutes = model_minutes.predict(X_test)

accuracy_points = mean_squared_error(y_test_points, y_pred_points)
accuracy_minutes = mean_squared_error(y_test_minutes, y_pred_minutes)

mae_points = mean_absolute_error(y_test_points, y_pred_points)
mae_minutes = mean_absolute_error(y_test_minutes, y_pred_minutes)

print("场均得分均方误差:",accuracy_points)
print("场均上场时间均方误差:",accuracy_minutes)
print("场均得分平均绝对误差:",mae_points)
print("场均上场时间平均绝对误差:",mae_minutes)