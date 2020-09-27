# Import libraries
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
import joblib
import os




app = Flask(__name__)
# Load the model
model = joblib.load('model.joblib')
@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    df = pd.DataFrame(data)
    # Make prediction using model loaded from disk as per the data.
    prediction = list(model.predict(df))
    # Take the first value of prediction
    #output = prediction[0]
    #return jsonify(prediction.tolist())
    return jsonify({'prediction': str(prediction)})
    

if __name__ == '__main__':
    #context=('cert.pem', 'key.pem')#certificate and key files
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run(port=5000, debug=True,ssl_context=context)
    #app.run(port=5000, debug=True,ssl_context='adhoc')