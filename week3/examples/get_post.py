# flask.Request
from flask import Flask, send_file, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
   return send_file("index.html")

@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    return f"Hello <b>{name}</b>!"

data = {
    "fruits":   ["apple","cherry", "grape", "watermelon"],  
    "cars":     ["ford f150", "toyota RAV4", "honda accord"],
    "jobs":     ["professor", "software engineer", "accountant"],
}

@app.route("/get/<key>", methods=["GET"])
def get(key):
    if key in data:
        return ", ".join(data[key])
    return "Invalid key"

@app.route("/post", methods=["POST"])
def post():
    key, value = request.form["key"], request.form["value"]
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]
    return redirect(url_for("index"))

if __name__ == "__main__":
   app.run(host="0.0.0.0",debug=True)

# firefox "$(hostname -I | xargs):5000/"
