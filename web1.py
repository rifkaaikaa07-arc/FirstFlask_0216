from flask import Flask
#from markupsafe import escape
app=Flask(__name__)
@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/")
def index():
    return "Welcome!"

@app.route("/hi/<name>")
def hi(name):
    return f"Hi, {name}!"

@app.route("/double/<int:n>")
def double(n):
    return f"{n * 2}"