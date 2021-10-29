#Import the required plugins
from flask import Flask, request, jsonify
from flask_restful import Api, Resource 
import pickle
import pandas as pd

#Step 1: Wrapping our app
app = Flask(__name__)
api = Api(app) #Wrapping o ur app in a restful API

#Step 1.5: Load the model
model = pickle.load(open('model.pkl', 'rb'))


#Step 2: Define our API Resources
class HelloWorld(Resource):
    
    def get(self):
        return {"hello":"world"}

class Predict(Resource):

    def post(self): #post request
        json_data = request.get_json()

        # For 1 observation 
        df = pd.DataFrame(json_data.values(), 
                       index = json_data.keys()).transpose()

        # How to take multiple observation
        # df = pd.DataFrame(json_data)
        
        result = model.predict(df)
        return result.tolist()


#Step 3: Assign our endpoints
api.add_resource(HelloWorld, '/helloworld')
api.add_resource(Predict,'/predict')



#Step 4: Runing our api app
if __name__ == '__main__': 
    app.run(debug=True)