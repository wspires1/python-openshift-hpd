from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return "version 0.0.1"

if __name__ = "__main__":
    app.run(host="0.0.0.0", port=8080)
