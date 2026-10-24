from pathlib import Path

import pandas as pd
from dash import Dash, Input, Output, dcc, html
import plotly.express as px

DATA = Path(__file__).with_name("airline_data.csv")
if DATA.exists():
    data = pd.read_csv(DATA, encoding="ISO-8859-1")
else:
    data = pd.DataFrame({"Month": [1, 2, 3, 4], "ArrDelay": [12, 18, 9, 24], "Reporting_Airline": ["A", "B", "A", "B"]})

app = Dash(__name__)
app.layout = html.Div([
    html.H1("Module 04 Lab 04 — Flight Delay Dashboard"),
    dcc.Dropdown(id="airline", options=[{"label": x, "value": x} for x in sorted(data["Reporting_Airline"].dropna().unique())], multi=True),
    dcc.Graph(id="delay-chart"),
])

@app.callback(Output("delay-chart", "figure"), Input("airline", "value"))
def update_chart(selected):
    frame = data if not selected else data[data["Reporting_Airline"].isin(selected)]
    grouped = frame.groupby("Reporting_Airline", as_index=False)["ArrDelay"].mean()
    return px.bar(grouped, x="Reporting_Airline", y="ArrDelay", title="Average Arrival Delay by Reporting Airline")

if __name__ == "__main__":
    app.run(debug=True)
