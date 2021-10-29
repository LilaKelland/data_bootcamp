# import Flask and jsonify
from flask import Flask, jsonify, request
# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

# endpoints
class Add(Resource):
    def get(self):
        # create request parser - parses optional arguments
        parser = reqparse.RequestParser()
        

        # create arguments  # OR SHOULD THIS BE A DICT? numbers {numbers: {number1: 1}, {number2: 2}}
        parser.add_argument('number1', type=float)
        parser.add_argument('number2', type=float)

        # parse 'numbers' - Store  argument
        number1 = parser.parse_args().get('number1')
        number2 = parser.parse_args().get('number2')
        # addition = number1 + number2

        if number1 and number2:
            addition = number1 + number2
        else:
            addition = 'Need to provide 2 numbers'

        # make json  
        return jsonify(addition=addition)

    def post(self):
        json_data = request.get_json()

        number1 = json_data['number1']
        number2 = json_data['number2']
        addition = number1 + number2
        return jsonify(addition=addition)


# endpoints
class Subtract(Resource):
    def get(self):
        # create request parser - parses optional arguments
        parser = reqparse.RequestParser()

        # create argument 
        parser.add_argument('number1', type=float)
        parser.add_argument('number2', type=float)

        # parse 'number1, number2' - Store argument
        number1 = parser.parse_args().get('number1')
        number2 = parser.parse_args().get('number2')

        # subtraction = number1 - number2
        if number1 and number2:
            subtraction = number1 - number2
        else:
            subtraction = 'Need to provide 2 numbers'



        # make json 
        return jsonify(subtraction=subtraction)

    def post(self):
        json_data = request.get_json()

        number1 = json_data['number1']
        number2 = json_data['number2']
        division = number1 -number2
        return jsonify(subtraction=subtraction)

# endpoints
class Divide(Resource):
    def get(self):
        # create request parser - parses optional arguments
        parser = reqparse.RequestParser()

        # create argument 
        parser.add_argument('number1', type=float)
        parser.add_argument('number2', type=float)

        # parse 'name' - Store name argument
        number1 = parser.parse_args().get('number1')
        number2 = parser.parse_args().get('number2')

        if number1 and number2:
            division = number1 /number2
        else:
            division = 'Need to provide 2 numbers'
        
        # division = number1 /number2

        # make json 
        return jsonify(division=division)
    
    def post(self):
        json_data = request.get_json()

        number1 = json_data['number1']
        number2 = json_data['number2']
        division = number1 /number2
        return jsonify(division=division)

# assign endpoint
api.add_resource(Add, '/add', methods = ['POST', 'GET'])
api.add_resource(Subtract, '/subtract', methods = ['POST', 'GET'])
api.add_resource(Divide, '/divide', methods = ['POST', 'GET'])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555, debug=True)
    # app.run(debug=True)


# http://127.0.0.1:5000/add?number1=4&number2=2 or pass in json for post as in test_calc.py

# http://ec2-3-23-132-27.us-east-2.compute.amazonaws.com:5555/add?number1=4&number2=2
