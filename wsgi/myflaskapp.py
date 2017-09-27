import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()
