import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import plotly.express as px #graphing
import missingno as msno #describe data
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/kaggle/input/nbaplayersdraft.csv")
print(df.shape)

df.info()

df.describe().style.background_gradient(cmap = "Blues")

plt.figure(figsize = (20,10))
sns.countplot(data=df,x="year");