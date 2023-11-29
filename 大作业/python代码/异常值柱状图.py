import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import plotly.express as px #graphing
import missingno as msno #describe data
import matplotlib.pyplot as plt

categories = ['1-10','10-20','20-30','30+']
values = [0.630,0.430,0.025,0.081]
colors = ['blue', 'green', 'yellow', 'orange']
plt.bar(categories,values,color=colors)
plt.xlabel('draft')
plt.ylabel('abnormal values percentage')
plt.title('')
plt.show()