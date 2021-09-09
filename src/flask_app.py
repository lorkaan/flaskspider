from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

if __name__ == '__main__':
    port = 5000
    host = "localhost"
    app.run(host=host, port=port)