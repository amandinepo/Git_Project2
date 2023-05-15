from dash import dcc,Dash, html, Input, Output,State
import plotly.express as px
import pandas as pd
import random

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__,external_stylesheets=external_stylesheets)

server = app.server

CourseQuestions = ["Which git command creates a Git repository inside your directory ?", 
                   "Which bash command downloads a file from an URL ?", 
                   "In git file system, a directory is called a...?",
                   "Which bash command allows to delete a file ?",
                   "Which bash command allows to display the elements in a folder ?",
                   "Which bash command allows to change folder ?",
                   "Which letter is used after a bash command is used to display ALL of the elements in a folder ?",
                   "Which git is command change files to another point in Git history ?",
                   "Which bash command prints working directory ?",
                   "What does sudo means ?",
                   "Which git command adds changes to local Git history ?",
                   "Which git command registers some changes for next commit ?",
                   "Which git command copies a distant repository ?",
                   "Which git command downloads Git objects from distant repository ?",
                   "Which git command fetches AND mergees from distant repository ?",
                   "Which git command sends Git objects to a distant repository ?",
                   "Which bash command allows to display the path for the command executable ?",
                   "What does apt means ?",
                   "Which symbol Pass a command output as input for the next one ?",
                   "What does bash means ?",
                   "What does sh means ?",
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
                 "substitute user do",
                 "git commit",
                 "git add",
                 "git clone",
                 "git fetch",
                 "git pull",
                 "git push",
                 "which",
                 "|",
                 "Bourne-Again shell",
                 "Bourne shell"
                 ]

i= random.randint(0,19)

app.layout = html.Div([
    html.Div(html.H1(children="Welcome to the Git,Python,Linux quiz")),
    html.Div(html.H2(id="Question_zone", children=CourseQuestions[i])),
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Button('Another question', id='change-question'),
    html.Div(id='container-button-basic',
             children=''),
    html.Div(id='container-button-basic2',
             children='Enter an answer and press submit')
])

@app.callback(Output('Question_zone', 'children'), [Input('change-question', 'n_clicks')], [State('input-on-submit', 'value')])
def refresh_page(n_clicks, i):
    if n_clicks is not None and n_clicks > 0:
        n_clicks = 0
    i = random.randint(0,19)
    return [html.H2(children=CourseQuestions[i] + " "+ str(i))]

@app.callback(
    Output('container-button-basic', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value')
)
def update_output(i, value):
    html.H2.children
    GoodAnswer = "Bonne réponse !"
    BadAnswer = "Dommage...La réponse était {}".format(CourseAnswers[i])
    Answer = "Entrez votre réponse"
    
    if(value != None):
        if(value == CourseAnswers[i]):
            Answer = GoodAnswer
        else:
            Answer = BadAnswer
    
    return Answer + " " + html.H2.children

if __name__ == '__main__':
    app.run_server(debug=True,port='8050')
