from dash import Dash, html

app = Dash(__name__)
app.layout = html.Div([
    html.H1("Module 04 Lab 02 — Dash Basics"),
    html.P("A minimal Dash layout using HTML components."),
    html.Ul([html.Li("Reusable layout components"), html.Li("Local development server")]),
])

if __name__ == "__main__":
    app.run(debug=True)
