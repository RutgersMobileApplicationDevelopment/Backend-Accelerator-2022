from flask import Flask, send_file
from flask_restx import reqparse, Api, Resource

app = Flask(__name__)
api = Api(doc=False)
api.init_app(app)

@app.route("/index")
def index():
    return send_file("forum.html")

posts = {
    "sample_id": []
}

parser = reqparse.RequestParser()
parser.add_argument("key")
parser.add_argument("value")


incr_id = 0

class UserPost(Resource):

    def get(self):
        args = parser.parse_args()
        post_id = args["key"]
        if post_id in posts:
            return posts[post_id], 200
        else:
            return "Post does not exist for id", 404

    def post(self):
        global incr_id
        args = parser.parse_args()
        post_id = args["key"]
        value = args["value"]
        if post_id == "":
            incr_id += 1
            print(incr_id)
            posts[str(incr_id)] = [value]
            return incr_id, 200
        else:
            if post_id in posts:
                posts[post_id].append(value)
                return post_id, 200 # add a comment to this post
            else:
                return "Post does not exist for id", 400

api.add_resource(UserPost, '/posts')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)