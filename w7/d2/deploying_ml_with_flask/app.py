from flask import Flask, jsonify, request
# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy
import pickle

app = Flask(__name__)
api = Api(app)

# At the beginning of the file, we need to create the same custom class we used in the model creation part.

class RawFeats:
    def __init__(self, feats):
        self.feats = feats

    def fit(self, X, y=None):
        pass

    def transform(self, X, y=None):
        return X[self.feats]

    def fit_transform(self, X, y=None):
        self.fit(X)
        return self.transform(X)

# Now, we will load our model (from pickle).

model = pickle.load( open( "model.p", "rb" ) )

# create an endpoint where we can communicate with our ML model - this time POST
class Scoring(Resource):
    def post(self):
        json_data = request.get_json()
        df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()
        # getting predictions from our model.
        # it is much simpler because we used pipelines during development
        res = model.predict_proba(df)
        # we cannot send numpt array as a result
        return res.tolist() 

# assign endpoint to api
api.add_resource(Scoring, '/scoring')

# The last thing to do is to create an application run when the file api.py is run directly (not imported as a module from another script).
if __name__ == '__main__':
    app.run(debug=True)