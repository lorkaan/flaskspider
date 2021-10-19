from flask import Flask, render_template, request
from static.httpspider.api.graph import createGraph as make_graph
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/search")
def search_page():
    return render_template("search.html", action="/results")

@app.route("/results", methods=["POST"])
def results_page():
    _, obj = make_graph([request.form.get('entry_point', "")], request.form.get('max_depth', 1))
    try:
        obj_str = json.dumps(obj)
    except Exception as e:
        obj_str = ""
    return obj_str

if __name__ == '__main__':
    port = 5000
    host = "localhost"
    app.run(host=host, port=port)