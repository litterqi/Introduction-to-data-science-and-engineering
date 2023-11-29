import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import plotly.express as px #graphing
import missingno as msno #describe data
import matplotlib.pyplot as plt
import os

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv("/kaggle/input/nbaplayersdraft.csv")

threshold =10 
selected_data = df[df['rank']<=threshold]

bins = [0,5,10,15,20,float('inf')]
labels = ['0-5','5-10','10-15','15-20','20+']

selected_data["points_per_game"] = pd.cut(selected_data['points_per_game'], bins=bins, labels=labels, right=False)

y=selected_data['points_per_game'].value_counts()
plt.figure(figsize=(5,5))
labels=['0-5','5-10','10-15','15-20','20+']
plt.pie(y,labels=labels,autopct='%1.1f%%')
plt.legend(loc='lower left')
plt.title('top 10 selected players distribution of points_per_game')
plt.show()