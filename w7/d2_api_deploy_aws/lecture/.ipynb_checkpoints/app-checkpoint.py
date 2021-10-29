from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import pandas as pd
import pickle

# step 1 wraping our app
app = Flask(__name__)
api = Api(app) 

# step 1.5 load model
model = pickle.load(open("model.pkl", 'rb'))

# step 2 define api resources
class HelloWorld(Resource):

    def get(self):
        return{"Hello":"world"}

class Predict(Resource):

    def post(self):
        json_data = request.get_json()
        
        # # only one at a time
        df = pd.DataFrame(json_data.values(),index = json_data.keys()).transpose()

        # how to make multiple predictions - print X_test.csv from original folder


        result = model.predict(df) # or predict_proba(df)
        return result.tolist(), 201 # can put staus code in


# step 3  assign endpoints
api.add_resource(HelloWorld, '/helloworld')
api.add_resource(Predict, '/predict')

# step 4: running our api app
if __name__ == '__main__':
    app.run(debug=True)