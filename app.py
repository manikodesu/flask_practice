from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
    return "<h1>Hello world!<h1>"

@app.route('/hello/<name>')
def grret(name):
    return f"<h1>Hello {name}!"

if __name__ == '__main__':
    app.run(debug=True)