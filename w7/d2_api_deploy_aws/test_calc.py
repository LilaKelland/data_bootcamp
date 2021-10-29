#  Python test file for flask to test locally
import requests as r
import pandas as pd
import json

base_url = "http://127.0.0.1:5000/" # base url local host
# base_url = 'http://ec.....com:8888/' #cloud base url

json_data = {
"number1":6,
"number2":2
}


response = r.post(base_url + 'divide', json = json_data) # send json data 

# multiple predictions
# respose = r.post(base_url +'predict', json = test)

if response.status_code == 200:
    print("...")
    print("request successful")
    print("...")
    print(response.json())
else:
    print("response failed")