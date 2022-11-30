from flask import Flask, send_file, redirect, render_template
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

class PostModel(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    poster = db.Column(db.VARCHAR(20), nullable=False)
    title = db.Column(db.VARCHAR(100), nullable=False)
    content = db.Column(db.VARCHAR(2000), nullable=False)

with app.app_context():
    db.create_all()

def is_valid_session(sessionId):
    return SessionModel.query.get(sessionId) != None

@app.route("/")
def index():
    if "sessionId" in session and session["sessionId"] != "" and is_valid_session(session["sessionId"]):
        return redirect("/dashboard")
    else:
        session["sessionId"] = None
        return redirect("/login")

@app.route("/login")
def login():
    return send_file("login.html")

@app.route("/register")
def register():
    return send_file("register.html")

@app.route("/logout")
def logout():
    if "sessionId" in session and is_valid_session(session["sessionId"]):
        db.session.delete(SessionModel.query.filter_by(sessionId=session["sessionId"]).one())
        db.session.commit()

    session["sessionId"] = None
    session["username"] = None

    return redirect("/login")

@app.route("/dashboard")
def dashboard(username = None):
    if "sessionId" not in session or session.get("sessionId") == None:
        return redirect("/login")

    return render_template("dashboard.html", username=session['username'])

@app.route("/posts/<post_id>")
def get_post(post_id):
    post_model = PostModel.query.get(post_id)
    if post_model:
        return render_template("post.html",
            post_id=post_model.id,
            poster=post_model.poster,
            post_title=post_model.title,
            post_content=post_model.content
        )
    else:
        return redirect("/dashboard")

@app.route("/browse")
def browse():
    post_models = PostModel.query.limit(10).all()
    transformed_posts = []
    if post_models:
        for post in post_models:
            transformed_posts.append({
                "title": post.title,
                "poster": post.poster,
                "id": post.id,
            })
        
        print(transformed_posts)

    return render_template("browse.html",
        posts = transformed_posts
    )

def generateSessionForUser( username ):
    if SessionModel.query.filter_by(username = username):
        SessionModel.query.filter_by(username=username).delete()
        db.session.commit()

    token = "".join(random.choices(string.ascii_lowercase+string.digits, k=64))

    session_model = SessionModel(
        token = token,
        username = username
    )

    db.session.add(session_model)
    db.session.commit()

    return token

@app.route("/api/login", methods=["POST"])
def api_login():
    username = request.form["username"]
    password = request.form["password"]

    if username != "" and password != "":
        user_model = UserModel.query.get(username)

        if user_model == None:
            return {"statusCode":401, "message":"Account with username does not exist"}

        if password == user_model.password:
            token = generateSessionForUser(username)
            session['username'] = username
            session["sessionId"] = token

            return redirect("/dashboard")

    else:
        return {"statusCode":401, "message":"Invalid credentials"}

    return {"statusCode":401}

@app.route("/api/post", methods=["POST"])
def api_post():
    if session.get("sessionId") in ("",None):
        return {"statusCode":401, "message":"Invalid credentials"}

    session_id = session["sessionId"]

    if not is_valid_session(session_id):
        return {"statusCode":401, "message":"Invalid session id"}

    title = request.form["title"]
    content = request.form["content"]

    post_model = PostModel(
        poster = session["username"],
        title = title,
        content = content
    )

    try:
        db.session.add(post_model)
        db.session.commit()

        return redirect(f"/posts/{post_model.id}")
    except Exception as e:
        return {"statusCode":"5XX", "message":"Internal server error"}



@app.route("/api/register", methods=["POST"])
def api_register():
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