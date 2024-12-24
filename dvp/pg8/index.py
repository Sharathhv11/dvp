from dash import Dash,dcc,html,Input,Output
import pandas as pd
import plotly.express as px

df = pd.read_csv("./data.csv")

app = Dash()

dropdown = dcc.Dropdown(options=df["Place"].unique(),value="BSE")

slider = dcc.Slider(min=df["Day"].min(),max=df["Day"].max(),step=1,value=df["Day"].min())

app.layout = html.H1(children=[
    html.H1(children="stock details"),
    dropdown,
    slider,
    dcc.Graph(id="graph"),
    dcc.Graph(id="bar")
])


@app.callback(
    [Output(component_id="graph",component_property="figure"),
     Output(component_id="bar",component_property="figure")],
    [Input(component_id=dropdown,component_property="value"),
     Input(component_id=slider,component_property="value")]
)
def dosomething(stock,day):
    filter = df[df["Place"] == stock]
    filter_range = df[df["Day"] == day]
    return px.line(filter,x="Date",y="Open",color="Symbol"),px.bar(filter_range,x="Date",y="Open",color="Symbol")

if( __name__ == "__main__" ):
    app.run_server(debug=True)