import plotly.express as px
import pandas as pd

df = pd.read_csv("./data.csv")

fig = px.line(
    df,
    x="timestamp",
    y="tempature",
    title="Temprature over the time",
    hover_data={
        "tempature":':.2f'
    }
)

fig.update_traces(
    mode="lines+markers",
    line=dict(color="blue",width=2),
    marker=dict(color="red",size=8)
)

fig.update_layout(
    xaxis_title="timestamp",
    yaxis_title="tempature",
    hovermode="x unified"
)

fig.update_xaxes(tickangle=30)
fig.show()

import plotly.io as pio
pio.renderers.default = "browser"