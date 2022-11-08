from flask import Flask, send_file, request
from flask_restx import reqparse, Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"

db = SQLAlchemy(app)

api = Api(doc=False)
api.init_app(app)

class RecipeModel(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    ingredients = db.Column(db.Text, nullable=False)
    poster = db.Column(db.VARCHAR(24), nullable=False)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "ingredients": self.ingredients.split(","),
            "poster": self.poster
        }

with app.app_context():
    db.create_all()

class RecipeResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("id", type=int)
    parser.add_argument("name", type=str)
    parser.add_argument("ingredients", type=str)
    parser.add_argument("poster", type=str)

    def get(self):
        args = self.parser.parse_args()
        print(args["id"])
        if args["id"]:
            recipe = RecipeModel.query.get(args["id"])
        else:
            recipe = RecipeModel.query.filter_by(name=args["name"]).first()
        return recipe.as_dict() if recipe else {}

    def post(self):
        args = self.parser.parse_args()
        ingredients = args["ingredients"].split(",")
        
        if args["name"] == "": return "No name was provided for recipe.", 400
        if len(args["ingredients"]) == 0: return "No ingredients were provided for recipe.", 400
        if args["poster"] == "": return "No poster was provided for recipe.", 400

        recipe = RecipeModel(
            name = args["name"],
            ingredients = args["ingredients"],
            poster = args["poster"]
        )

        try:
            db.session.add(recipe)
            db.session.commit()
            return {"statusCode":"OK","id":recipe.id}, 200
        except Exception as e:
            return {"statusCode":500,"message":repr(e)}, 500

api.add_resource(RecipeResource, '/recipes')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Nunc at augue id lorem sagittis laoreet ac sit amet elit.
# Suspendisse lacinia, turpis malesuada dapibus lobortis.