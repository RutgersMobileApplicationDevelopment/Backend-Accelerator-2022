from flask import Flask, send_file, redirect, flash
from flask import session, request
from flask_sqlalchemy import SQLAlchemy

import random, string

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "RUMAD-WEEK-6"

db = SQLAlchemy(app)

class UserModel(db.Model):
    username = db.Column(db.VARCHAR(20), nullable=False, unique=True, primary_key=True)
    password = db.Column(db.VARCHAR(32), nullable=False)

class SessionModel(db.Model):
    token = db.Column(db.VARCHAR(64), nullable=False, unique=True, primary_key=True)
    username = db.Column(db.VARCHAR(20), nullable=False)

with app.app_context():
    db.create_all()

def createSessionForUser(username):
    session_token = "".join(random.choices( string.ascii_lowercase + string.digits, k = 64 ))
    session_model = SessionModel(token=session_token, username=username)

    db.session.add(session_model)
    
    return session_token

@app.route("/")
def index():
    if "sessionId" in session:
        return redirect("/dashboard")
    else:
        return redirect("/login")

@app.route("/login")
def login():
    return send_file("login.html")

@app.route("/register")
def register():
    return send_file("register.html")

@app.route("/dashboard")
def dashboard():
    if not "sessionId" in session:
        return redirect("/login")
    return f"""
<html>
    <body>
        <h1>Welcome {session["username"]}</h1>
        <a href="/logout"/><input type="button" value="Logout"> </input></a>
    </body>
</html>
    """

@app.route("/api/login",methods=["POST"])
def post_login():
    user, pw = request.form["username"], request.form["password"]
    user_model = UserModel.query.get(user)
    if user_model:
        session_token = createSessionForUser(user)
        session["sessionId"] = session_token
        session["username"] = user
        return redirect("/dashboard")
    else:
        return {"statusCode":401,"message":"Invalid credentials"}

@app.route("/api/register",methods=["POST"])
def post_register():
    user, pw = request.form["username"], request.form["password"]
    
    if not UserModel.query.get(user):
        user_model = UserModel(
            username = user,
            password = pw
        )
        try:
            db.session.add(user_model)
            db.session.commit()
            return {"statusCode":200,"message":"OK"}
        except Exception as e:
            print(repr(e))
            return {"statusCode":500, "message":"Unknown internal server error occurred"}
    else:
        return {"statusCode":401,"message":"Username is already in use."}

@app.route("/logout")
def post_logout():
    if "sessionId" in session:
        record = SessionModel.query.get(session["sessionId"])

        if record:
            db.session.delete(record)
            db.session.commit()

        del session["sessionId"]
        del session["username"]
        

    return redirect("/")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)