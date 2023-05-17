from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    mountains = ['Everest', 'K2', 'Kilimanjaro']
    return render_template('index.html', mountain=mountains)

@app.route('/mountain/<mt>')
def mountain(mt):
    return "This is " + str(mt)

if __name__ == "__main__":
    app.run_server(host='68.219.114.168', port='8050')
