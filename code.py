import pandas as pd
import csv
import plotly.graph_objects as gobj

df = pd.read_csv("student_data.csv")
print(df.groupby("level")["attempt"].mean())

fig = gobj.Figure(gobj.Bar(
    x = df.groupby("level")["attempt"].mean(),
    y = ['level 1','level 2','level 3','level 4'],
    orientation = 'h'
))

fig.show()