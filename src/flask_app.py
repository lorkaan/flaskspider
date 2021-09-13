from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/search")
def search_page():
    return render_template("search.html", action="/results")

@app.route("/results")
def results_page():
    return "Results will go here"

if __name__ == '__main__':
    port = 5000
    host = "localhost"
    app.run(host=host, port=port)