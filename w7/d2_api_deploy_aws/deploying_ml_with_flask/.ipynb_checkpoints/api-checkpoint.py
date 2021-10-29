{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ac228342-9b41-43ec-802c-b17bbd55c636",
   "metadata": {},
   "outputs": [],
   "source": [
    "# import Flask and jsonify\n",
    "from flask import Flask, jsonify, request\n",
    "# import Resource, Api and reqparser\n",
    "from flask_restful import Resource, Api, reqparse\n",
    "import pandas as pd\n",
    "import numpy\n",
    "import pickle\n",
    "\n",
    "app = Flask(__name__)\n",
    "api = Api(app)\n",
    "\n",
    "# need custom class used in model and stored in pickle file and used in scoring as well.\n",
    "# The accesses to other sklearn modules are provided automatically and we don't have to do anything about them in the scoring file.\n",
    "\n",
    "class RawFeats:\n",
    "    def __init__(self, feats):\n",
    "        self.feats = feats\n",
    "\n",
    "    def fit(self, X, y=None):\n",
    "        pass\n",
    "\n",
    "\n",
    "    def transform(self, X, y=None):\n",
    "        return X[self.feats]\n",
    "\n",
    "    def fit_transform(self, X, y=None):\n",
    "        self.fit(X)\n",
    "        return self.transform(X)\n",
    "\n",
    "# Now, we will load our model (from pickle).\n",
    "\n",
    "model = pickle.load( open( \"model.p\", \"rb\" ) )\n",
    "\n",
    "# create an endpoint where we can communicate with our ML model (POST this time)\n",
    "\n",
    "class Scoring(Resource):\n",
    "    def post(self):\n",
    "        json_data = request.get_json()\n",
    "        df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()\n",
    "        # getting predictions from our model.\n",
    "        # it is much simpler because we used pipelines during development\n",
    "        res = model.predict_proba(df)\n",
    "        # we cannot send numpt array as a result\n",
    "        return res.tolist() \n",
    "    \n",
    "# assign endpoint\n",
    "api.add_resource(Scoring, '/scoring')\n",
    "\n",
    "# The last thing to do is to create an application run when the file api.py \n",
    "# is run directly (not imported as a module from another script).\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "bootcamp_env",
   "language": "python",
   "name": "bootcamp_env"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
