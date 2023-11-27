import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import plotly.express as px #graphing
import missingno as msno #describe data
import os

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv("/kaggle/input/nbaplayersdraft.csv")

df0 = df[df["games"] > 250]

fig = px.scatter_3d(df0, x = "year", y = "overall_pick", z = "points", 
                    opacity = 0.75, hover_data = ["player"],
                    color = "overall_pick", color_continuous_scale = "haline_r")

fig.update_traces(marker = dict(size = 3.5)) # scaling down the markers
fig.update_layout(template = "plotly_dark", font = dict(family = "PT Sans", size = 12))
fig.show()