#Import the required plugins
from flask import Flask, request, jsonify
from flask_restful import Api, Resource 
import pickle
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import FunctionTransformer

app = Flask(__name__)
api = Api(app) #Wrapping o ur app in a restful API

# Load the model

# Custom functions -----------------------------------------
cat_feats = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Credit_History', 'Property_Area']
num_feats = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term']

def numFeat(data):
    return data[num_feats]

def catFeat(data):
    return data[cat_feats]

def inject_features(data):
    data['Total_Income_Log'] = np.log(data['ApplicantIncome'] + data['CoapplicantIncome'])
    data['LoanAmt_Term_Ratio_Log']=  np.log(data['LoanAmount']/data['Loan_Amount_Term'])
    data['LoanAmount_Log'] = np.log(data['LoanAmount'])
    data.drop(labels=['ApplicantIncome','CoapplicantIncome', 'LoanAmount'], axis=1, inplace=True)
    data.reset_index(inplace=True)
    return data

def fill_null(data):
    fill_NaN = SimpleImputer(missing_values=np.nan, strategy='median')
    imputed = pd.DataFrame(fill_NaN.fit_transform(data))
    imputed.columns = data.columns
    imputed.index = data.index
    return imputed

# keep_num = FunctionTransformer(numFeat)
# keep_cat = FunctionTransformer(catFeat)
# fill_null = FunctionTransformer(fill_null)    
# injected_features = FunctionTransformer(inject_features)
#-----------------------------------------------------------------
model = pickle.load(open('rf_pipeline.pickle', 'rb'))

# API Resources
class HelloWorld(Resource):
    
    def get(self):
        return {"hello":"world"}

class Predict(Resource):

    def post(self): #post request
        json_data = request.get_json()


        df = pd.json_normalize(json_data)
        # df = pd.DataFrame(json_data.values(), 
        #                index = json_data.keys()).transpose()
        print(df)
        print(df.dtypes)
        
        result = model.predict(df)
        if result[0] == 0:
            return({'result': "Sorry you are not approved."})
        elif result[0] == 1:
            return({'result': "You have been approved!"})
        else:
            print(result[0])
            return result.tolist()


# Assign endpoints
api.add_resource(HelloWorld, '/')
api.add_resource(Predict,'/predict')


if __name__ == '__main__': 
    # app.run(debug=True)
    app.run(host='0.0.0.0')