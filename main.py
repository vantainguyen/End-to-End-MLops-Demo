import pickle 
from flask import Flask, request, jsonify
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

if __name__ == '__main__':
	app.run(debug=True)