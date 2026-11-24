
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
    app.run(debug=True)

@app.route("/")
def home():
    return "Home page"

@app.route("/about")
def about():
    return "About us"

@app.route("/user/<name>")
def profile(name):
    return f"Hello, {name}!"

@app.route("/post/<int:post_id>")
def post(post_id):
    post_id=post_id+15
    return f"Post #{post_id}"

@app.route("/")
def index():
    return "Welcome!"

@app.route("/hi/<name>")
def hi(name):
    return f"Hi, {name}!"

@app.route("/double/<int:n>")
def double(n):
    return f"{n * 2}"