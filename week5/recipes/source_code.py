# This code is written in preparation for the weekly meeting.
# If you'd like to see the code written in the meeting,
# please see "live_code.py"

from flask import Flask, send_file, request, abort
from flask_restx import reqparse, Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"

db = SQLAlchemy(app)

api = Api()
api.init_app(app)

RecipeMarshal = api.model('Recipe',{
    'id': fields.Integer,
    'name': fields.String,
    'ingredients': fields.String,
    'poster': fields.String
})

class RecipeModel(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    ingredients = db.Column(db.Text, nullable=False)
    poster = db.Column(db.VARCHAR(24), nullable=False)


with app.app_context():
    db.create_all()

@api.route('/recipes')
class RecipeResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("id", type=int)
    parser.add_argument("name", type=str)
    parser.add_argument("ingredients", type=str)
    parser.add_argument("poster", type=str)

    @api.doc(params={"id": "The ID of the recipe to query for."})
    # @api.response(200, "Success", RecipeMarshal)
    # @api.response(400, "Invalid recipe ID")
    @api.marshal_with(RecipeMarshal)
    def get(self):
        args = self.parser.parse_args()

        if args["id"]:
            recipe = RecipeModel.query.get(args["id"])

        if not recipe:
            abort(400, 'Invalid recipe ID.')

        return recipe

    @api.doc(body=RecipeMarshal)
    @api.response(200, "Success", RecipeMarshal)
    @api.response(500, "Unexpected database connector error")
    def post(self):
        args = self.parser.parse_args()
        
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
            return {"message":"OK","id":recipe.id}, 200
        except Exception as e:
            abort(500)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)