import os
import logging
import numpy as np
from flask import Flask, request, jsonify
from sklearn.metrics import r2_score
from simple_linear_regr import SimpleLinearRegression
from utils import load_model, save_model, read_metrics, write_metrics

# Configure logging to save messages to a file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()  # Optional: Also print log messages to console
    ]
)

try:
    model = SimpleLinearRegression()
    app = Flask(__name__)
except Exception as e:
    logging.error(f'Exception: {e}')

model_path = os.path.join('artifacts', 'model.pkl')
metrics_path = os.path.join('artifacts', 'metrics.txt')

@app.route('/stream', methods=['POST'])
def inferenceStream():
    try:
        # Retrieve the input data from the request
        input_data = request.json['data']
        model = load_model(model_path)
        logging.info('loading model successfully for stream inference')
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
        model = load_model(model_path)
        logging.info('loading model successfully for batch inference')
        predicted = model.predict(input_data)
        response = {'result': predicted.tolist()}
        return jsonify(response)
    except Exception as e:
        logging.error(f'Exception: {e}')
    

@app.route('/train', methods=['POST'])
def train():
    try:
        # Retrieve the input data from the request
        input_data = request.json['data']
        model = SimpleLinearRegression(input_data['hyperparameters'][0], input_data['hyperparameters'][1])
        model = load_model(model_path)
        logging.info('loading existing model successfully')
        model.fit(np.array(input_data['X_train']), np.array(input_data['y_train']))
        predicted = model.predict(np.array(input_data['X_test']))
        r2_new = r2_score(np.array(input_data['y_test']), predicted)
        r2_best = read_metrics(metrics_path)
        if r2_new > r2_best:
            # save model
            save_model(model_path, model)
            result = f'New model was better. It was saved. Old r2: {r2_best:.4f}; new r2: {r2_new:.4f}'
            write_metrics(metrics_path, r2_new)
        else:
            result = f'New model is not better. It was not saved. Old r2: {r2_best:.4f}; new r2: {r2_new:.4f}'
        response = {'result': result}
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

    while True:
        try:
            app.run(debug=True)
        except Exception as e:
            logging.info(f'Exception: {e}')
            pass