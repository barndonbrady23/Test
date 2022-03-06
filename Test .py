from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>How Are YOU?</p>"

@app.route("/hello")
def hello_route():
    return "<p>Hello!</p>"
    