from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)

class RecipeModel(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    ingredients = db.Column(db.Text, nullable=False)
    poster = db.Column(db.VARCHAR(24), nullable=False)

with app.app_context():
    db.create_all()

    db.session.add(RecipeModel(
        name="pancakes",
        ingredients="flour,baking powder,sugar,salt,milk,butter,egg",
        poster="John Doe"    
    ))

    db.session.add(RecipeModel(
        name="muffins",
        ingredients="flour,baking powder,sugar,salt,milk,vegetable oil,egg",
        poster="Jane Doe"    
    ))

    # db.session.delete(RecipeModel(...))

    ### update a resource
    ### from https://stackoverflow.com/a/6701188
    # recipe = User.query.filter_by(name='admin').first()
    # admin.email = 'my_new_email@example.com'
    # db.session.commit()
    
    ### query for a resource by primary key
    # recipe = RecipeModel.query.get(5)
    # recipe.name = 'New name'
    # db.session.commit()

    ### get RecipeModel using filter_by function

    # queries can return multiple, so get the first!
    # if we want all, we use .all() instead
    
    # recipe = RecipeModel.query.filter_by(id=1).first()
    # recipes_by_john = RecipeModel.query.filter_by(poster="John Doe").all()

    # get RecipeModel by primary key
    # RecipeModel.query.get(1)
