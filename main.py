import os
import logging
from flask import Flask, request, jsonify
from simple_linear_regr import SimpleLinearRegression
from utils import load_model

# Configure logging to save messages to a file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()  # Optional: Also print log messages to console
    ]
)

# Configure path to artifacts
model_path = os.path.join('artifacts', 'model.pkl')
metrics_path = os.path.join('artifacts', 'metrics.txt')

try:
    model = SimpleLinearRegression()
    model = load_model(model_path)
    logging.info('loading model successfully for stream inference')
    app = Flask(__name__)
except Exception as e:
    logging.error(f'Exception: {e}')

@app.route('/stream', methods=['POST'])
def inferenceStream():
    try:
        # Retrieve the input data from the request
        input_data = request.json['data']
        predicted = model.predict(input_data)
        response = {'result': predicted[0][0]}
        return jsonify(response)
    except Exception as e:
        logging.error(f'Exception: {e}')

@app.route('/batch', methods=['POST'])
def inferenceBatch():
    try:
        # Retrieve the input data from the request
        input_data = request.json['data']
        predicted = model.predict(input_data)
        response = {'result': predicted.tolist()}
        return jsonify(response)
    except Exception as e:
        logging.error(f'Exception: {e}')
    
    
@app.route('/log')
def log():
    file = open('app.log', 'r') 
    result = file.readlines()
    file.close()
    response = {'result': result}
    return jsonify(response)

if __name__ == '__main__':

    app.run('0.0.0.0', '8080', debug=True)

    
