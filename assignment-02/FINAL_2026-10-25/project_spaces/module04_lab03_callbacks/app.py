from dash import Dash, Input, Output, dcc, html

app = Dash(__name__)
app.layout = html.Div([
    html.H1("Module 04 Lab 03 — Callback Interactivity"),
    dcc.Slider(id="value-slider", min=0, max=100, value=50, step=10),
    html.Div(id="slider-output", style={"marginTop": "20px", "fontSize": "24px"}),
])

@app.callback(Output("slider-output", "children"), Input("value-slider", "value"))
def show_value(value):
    return f"Selected value: {value}"

if __name__ == "__main__":
    app.run(debug=True)
