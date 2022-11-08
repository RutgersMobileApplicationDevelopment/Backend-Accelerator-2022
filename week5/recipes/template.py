from flask import Flask, send_file, request
from flask_restx import reqparse, Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"

db = SQLAlchemy(app)

api = Api()
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
    # Create request parser and add arguments

    def get(self):
        # Parse arguments
        # Verify that "id" is in arguments
        # - if "id" is in arguments, then get it
        # If we weren't able to set recipe, then abort(400, "msg")
        pass

    def post(self):
        # Parse arguments
        # Verify that all fields exist (name, ingredients, poster)

        # Create a recipe from the given fields
        
        # Add this recipe to the database and return success
        # However, we must handle exceptions
        # If we come across any unexpected behavior, abort(500)

        pass

api.add_resource(RecipeResource, '/recipes')
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)