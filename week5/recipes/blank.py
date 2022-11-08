from flask import Flask, send_file, request
from flask_restx import reqparse, Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"

db = SQLAlchemy(app)

api = Api(doc=False)
api.init_app(app)

class RecipeModel(db.Model):
    # column 0: id,             type: integer,  primary_key = true
    # column 1: name,           type: text,     unique = true
    # column 2: ingredients,    type: text
    # column 3: poster,         type: VARCHAR(24)
    pass

with app.app_context():
    db.create_all()

class RecipeResource(Resource):
    def get():
        pass

    def post():
        pass

api.add_resource(RecipeResource, '/recipes')
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)