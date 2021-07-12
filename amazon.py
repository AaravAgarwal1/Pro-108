import plotly.figure_factory as ff #new module
import csv
import pandas as pd

df=pd.read_csv("amazon_data.csv")

fig=ff.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"],show_hist=False) 

fig.show()
