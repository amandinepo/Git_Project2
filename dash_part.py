from dash import dcc,Dash, html, Input, Output,State
import plotly.express as px
import pandas as pd
import random

app = Dash(__name__)

CourseQuestions = ["Which git command creates a Git repository inside your directory ?", 
                   "Which bash command downloads a file from an URL ?", 
                   "In git file system, a directory is called a...?",
                   "Which bash command allows to delete a file ?",
                   "Which bash command allows to display the elements in a folder ?",
                   "Which bash command allows to change folder ?",
                   "Which letter is used after a bash command is used to display ALL of the elements in a folder ?",
                   "Which git is command change files to another point in Git history ?",
                   "Which bash command prints working directory ?",
                   "What does sudo means ?"
                   ]

CourseAnswers = ["git init",
                 "wget",
                 "tree",
                 "rm -r",
                 "ls",
                 "cd",
                 "a",
                 "git checkout",
                 "pwd",
                 "substitute user do"]

i= random.randint(0,9)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
])

app.layout = html.Div([
    html.Div(html.H1(children=CourseQuestions[i])),
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Button('Another question', id='change-question', n_clicks=0),
    html.Div(id='container-button-basic',
             children='Enter a value and press submit')
])


@app.callback(
    Output('container-button-basic', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value')
)
def update_output(n_clicks, value):
    return 'The answer was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    )

app.run_server(debug=True)