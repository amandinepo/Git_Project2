from dash import dcc,Dash, html, Input, Output,State
import plotly.express as px
import pandas as pd

app = Dash(__name__)

CourseQuestions = ["Which git command creates a Git repository inside your directory ?", 
                   "Name the three operating systems", 
                   "In git file system, a directory is called a...?",
                   ]

app.layout = html.Div([
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='container-button-basic',
             children='Enter a value and press submit')
])


@app.callback(
    Output('container-button-basic', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value')
)
def update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
)

app.run_server(debug=True)
