from flask import Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0')

@app.route('/')
def hello_world():
    return 'Hello World!'

  
