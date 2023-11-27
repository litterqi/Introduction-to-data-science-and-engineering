import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import plotly.express as px #graphing
import missingno as msno #describe data
import os

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv("/kaggle/input/nbaplayersdraft.csv")

df0 = df[df["games"] > 0]

sorted_df = df0.sort_values(by = "overall_pick", ascending = True)

fig = px.scatter_3d(sorted_df, x = "games", y = "year", z = "points_per_game",
                    range_x = (0, 1500), range_z = (0, 30),
                    hover_data = ["player"], animation_frame = "overall_pick", 
                    range_color = (0, 25), color = "points_per_game", color_continuous_scale = "jet")

fig.update_traces(marker = dict(size = 5)) # scaling down the markers
fig.update_layout(template = "plotly_dark", font = dict(family = "PT Sans", size = 12))
fig.show()