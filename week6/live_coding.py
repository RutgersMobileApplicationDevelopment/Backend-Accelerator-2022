from flask import Flask, send_file, redirect, flash
from flask import session, request
from flask_sqlalchemy import SQLAlchemy

import random, string

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db2.sqlite"
app.config["SECRET_KEY"] = "RUMAD-WEEK-6"

db = SQLAlchemy(app)

class UserModel(db.Model):
    username = db.Column(db.VARCHAR(20), nullable=False, primary_key=True)
    password = db.Column(db.VARCHAR(64), nullable=False)

class SessionModel(db.Model):
    token = db.Column( db.CHAR(64), nullable=False, primary_key=True )
    username = db.Column( db.VARCHAR(20), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    if "sessionId" in session and session["sessionId"] != "":
        return redirect("/profile")
    return redirect("/login")

@app.route("/login")
def login():
    return send_file("login.html")

@app.route("/register")
def register():
    return send_file("register.html")

@app.route("/logout")
def logout():

    session["sessionId"] = None

    return redirect("/login")

@app.route("/profile")
def profile():
    if "sessionId" not in session or session.get("sessionId") == None:
        return redirect("/login")

    return f"""
<html>
<body>
<h1>Hello!</h1>
<p>Your session id is {session["sessionId"]} </p>
<a href="/logout"/><input type="button" value="Logout"> </input></a>
</body>
</html>
"""

def generateSessionForUser( username ):
    token = "".join(random.choices(string.ascii_lowercase+string.digits, k=64))

    session_model = SessionModel(
        token = token,
        username = username
    )

    db.session.add(session_model)
    db.session.commit()

    return token

@app.route("/api/login", methods=["POST"])
def post_login():
    username = request.form["username"]
    password = request.form["password"]

    if username != "" and password != "":
        user_model = UserModel.query.get(username)

        if user_model == None:
            return {"statusCode":401, "message":"Invalid credentials"}

        if password == user_model.password:
            token = generateSessionForUser(username)
            session["sessionId"] = token

            return redirect("/profile")

    else:
        return {"statusCode":401, "message":"Invalid credentials"}

    return {"statusCode":401}

@app.route("/api/register", methods=["POST"])
def post_register():
    username = request.form["username"]
    password = request.form["password"]

    if username != "" and password != "":
        
        if UserModel.query.get(username) != None:
            return {"statusCode": 400, "message":"Username is already in use."}

        user_model = UserModel(
            username = username,
            password = password
        )

        try:
            db.session.add(user_model)
            db.session.commit()
        except Exception as e:
            return {"statusCode":"5XX", "message":"Internal server error"}

        return {"statusCode":200, "message":"OK"}

    return {"statusCode":400, "message":"Invalid parameters"}
    


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)