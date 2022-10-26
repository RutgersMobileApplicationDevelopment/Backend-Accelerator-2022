from flask import Flask, send_file
from flask_restx import reqparse, Api, Resource

app = Flask(__name__)
api = Api(doc=False)
api.init_app(app)

@app.route("/index")
def index():
    return send_file("index2.html")

data = {
    "fruits":   ["apple","cherry", "grape", "watermelon"],  
    "cars":     ["ford f150", "toyota RAV4", "honda accord"],
    "jobs":     ["professor", "software engineer", "accountant"],
}

parser = reqparse.RequestParser()
parser.add_argument("key")
parser.add_argument("value")

class my_resource(Resource):
    def get(self):
        args = parser.parse_args()
        if args["key"] in data:
            return data[args["key"]], 200
        return "Data could not be found for key", 404

    def post(self):
        args = parser.parse_args()
        key, value = args["key"], args["value"]
        if key in data:
            if value in data[key]:
                return "Value already exists for category", 400
            else:
                data[key].append(value)
        else:
            data[key] = [value]
        return "Data was successfully added",200

api.add_resource(my_resource, '/resource')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)