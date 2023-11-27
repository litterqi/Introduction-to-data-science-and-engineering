import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import plotly.express as px #graphing
import missingno as msno #describe data
import os

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv("/kaggle/input/nbaplayersdraft.csv")

fig = px.scatter(df, x = "overall_pick", y = "year", hover_data = ["player", "team"],
                 color = "points_per_game", color_continuous_scale = "Jet",
                 title = f"NBA Draft Points Per Game by Year and Overall Pick")

fig.update_traces(marker = dict(size = 8, symbol = "square")) # scaling the markers
fig.update_layout(template = "plotly_dark", font = dict(family = "PT Sans", size = 20))
fig.show()