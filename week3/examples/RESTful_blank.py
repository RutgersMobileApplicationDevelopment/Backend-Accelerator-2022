from flask import Flask, send_file
from flask_restx import reqparse, Api, Resource

app = Flask(__name__)
api = Api(doc=False)
api.init_app(app)

@app.route("/index")
def index():
    return send_file("index2.html")

data = {}

parser = reqparse.RequestParser()
#parser.add_argument("key")

class my_resource(Resource):
    def get(self):
        pass

    def post(self):
        pass

#api.add_resource(my_resource, '/resource')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)