from flask import Flask, send_file
from flask_restx import reqparse, Api, Resource

app = Flask(__name__)
api = Api(doc=False)
api.init_app(app)


@app.route("/index")
def index():
    return send_file("index2.html")


data = {
    "fruits":   ["apple", "cherry", "grape", "watermelon"],
    "cars":     ["ford f150", "toyota RAV4", "honda accord"],
    "jobs":     ["professor", "software engineer", "accountant"],
}

parser = reqparse.RequestParser()
parser.add_argument("key")
parser.add_argument("value")


class Group(Resource):
    def get(self):
        args = parser.parse_args()
        group_name = args['key']
        if not group_name:
            return data
        else:
            if group_name in data:
                return data[group_name], 200
            else:
                return {"message": "Could not find group for specified key", "status": 400}

    def post(self):
        args = parser.parse_args()
        key, value = args['key'], args['value']
        if key in data:
            if not value in data[key]:
                data[key].append(value)
                return {"message": "Resource was successfully added to group", "statusCode": 200}
            else:
                return {"message": "This resource already exists within the specified group.", "status": 400}
        else:
            return {"message": "Could not find group for specified key", "status": 400}


api.add_resource(Group, '/groups')
#api.add_resource(Group, '/groups/<string:name>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

