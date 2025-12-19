from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_word():
    return '<h1> Hello World</h1>'

@app.route('/about')
def about_page():
    return '<h1> About Page </h1>'