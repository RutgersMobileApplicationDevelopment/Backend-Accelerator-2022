from flask import Flask
app = Flask(__name__)

@app.route("/hello_world")
def hello_world():
   return "hello"

@app.route("/")
def hello_world():
   return "index"

if __name__ == "__main__":
   app.run(host="0.0.0.0")

# firefox "$(hostname -I | xargs):5000/hello_world"
