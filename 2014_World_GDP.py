import chart_studio.plotly as py
import plotly.graph_objects as go
from plotly.offline import iplot
import pandas as pd

df = pd.read_csv("2014_World_GDP.csv")
print(df.columns)

#the data for choropleth
mydata = dict(type="choropleth",
            locations=df["CODE"],
            locationmode = "ISO-3",
            z = df["GDP (BILLIONS)"],
            text = df["COUNTRY"],
            colorbar = {"title":"GDP IN BILLIONS"},
            marker = dict(line = dict(color = "rgb(255,255,255)", width = 1))
            )
mylayout = dict(title="2014 World GDP",
            geo = dict(scope="world", showlakes=True, lakecolor = "rgb(85,173,240)", showframe=False)
            )

myChoroMap = go.Figure(data=[mydata], layout=mylayout)
iplot(myChoroMap)
