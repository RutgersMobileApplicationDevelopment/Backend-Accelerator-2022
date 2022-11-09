from flask import Flask, send_file, request, abort
from flask_restx import reqparse, Api, Resource, fields, marshal
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"

db = SQLAlchemy(app)

api = Api()
api.init_app(app)

class RecipeModel(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    ingredients = db.Column(db.Text, nullable=False)
    poster = db.Column(db.VARCHAR(24), nullable=False)

RecipeMarshal = api.model('Recipe',{
    'id': fields.Integer,
    'name': fields.String,
    'ingredients': fields.String,
    'poster': fields.String
})

with app.app_context():
    db.create_all()

class RecipeResource(Resource):
    # Create request parser and add arguments
    parser = reqparse.RequestParser()
    parser.add_argument("id", type=int)
    parser.add_argument("name", type=str)
    parser.add_argument("ingredients", type=str)
    parser.add_argument("poster", type=str)

    @api.marshal_with(RecipeMarshal)
    @api.doc(params={"id": "The ID of the recipe to query for."})
    def get(self):
        args = self.parser.parse_args()

        if args["id"]:
            recipe = RecipeModel.query.get(args["id"])

            if recipe:
                return recipe
            else:
                abort(400,"Could not find recipe with id.")
        else:
            abort(400, "Did not specify id for recipe.")

        # Parse arguments
        # Verify that "id" is in arguments
        # - if "id" is in arguments, then get it
        # If we weren't able to set recipe, then abort(400, "msg")
        pass
    
    @api.doc(body=RecipeMarshal)
    def post(self):
        args = self.parser.parse_args()

        if not args["name"]:
            abort(400,"Did not specify name for recipe")

        if not args["ingredients"]:
            abort(400,"Did not specify ingredients for recipe")

        if not args["poster"]:
            abort(400,"Did not specify poster for recipe")
        
        recipe = RecipeModel(
            name = args["name"],
            ingredients = args["ingredients"],
            poster = args["poster"]
        )

        db.session.add(recipe)
        db.session.commit()

        return {
            "id": recipe.id
        }

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