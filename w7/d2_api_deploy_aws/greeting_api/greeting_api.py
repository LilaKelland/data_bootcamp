# import Flask and jsonify
from flask import Flask, jsonify

# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse
app = Flask(__name__)
api = Api(app)

# endpoints
class Greet(Resource):
    def get(self):
        # create request parser - parses optional arguments
        parser = reqparse.RequestParser()

        # create argument 'name'
        parser.add_argument('name', type=str)

        # parse 'name' - Store name argument
        name = parser.parse_args().get('name')

        if name:
            greeting = f'Hello {name}!'
        else:
            greeting = 'Hello person without name!'

        # make json from greeting string 
        return jsonify(greeting=greeting)

# assign endpoint
api.add_resource(Greet, '/greet',)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8080, debug=True, ) # run on computer

    # note if pass name in url like: http://127.0.0.1:5000/greet?name=John then response will {
#   "greeting": "Hello John!"
# }