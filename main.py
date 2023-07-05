import pickle 
import numpy as np
from flask import Flask, request, jsonify
from sklearn.metrics import r2_score
from simple_linear_regr import SimpleLinearRegression



model = SimpleLinearRegression()
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/stream', methods=['POST'])
def inferenceStream():
    # Retrieve the input data from the request
    input_data = request.json['data']
    predicted = model.predict(input_data)
    response = {'result': predicted[0][0]}
    return jsonify(response)

@app.route('/batch', methods=['POST'])
def inferenceBatch():
    # Retrieve the input data from the request
    input_data = request.json['data']
    predicted = model.predict(input_data)
    response = {'result': predicted.tolist()}
    return jsonify(response)

@app.route('/train', methods=['POST'])
def train():
    # Retrieve the input data from the request
    input_data = request.json['data']
    model.fit(np.array(input_data['X_train']), np.array(input_data['y_train']))
    predicted = model.predict(np.array(input_data['X_test']))
    r2_new = r2_score(np.array(input_data['y_test']), predicted)
    with open('metrics.txt', 'r') as file:
        r2_best = float(file.readline())
    if r2_new > r2_best:
        # save model
        with open('model.pkl', 'wb') as file:
            pickle.dump(model, file)
        result = 'New model is better. It has been saved'
        with open('metrics.txt', 'w') as file:
            file.write(str(r2_new))
    else:
        result = 'New model is not better. It was not saved'

    response = {'result': result}
    return jsonify(response)

if __name__ == '__main__':
	app.run(debug=True)