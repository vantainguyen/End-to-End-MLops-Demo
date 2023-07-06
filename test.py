import requests
from simple_linear_regr_utils import generate_data


X_train, y_train, X_test, y_test = generate_data()

# Define the input data
# input_data = {'X_train': X_train.tolist(), 'X_test': X_test.tolist(), 
# 'y_train': y_train.tolist(), 'y_test': y_test.tolist(), 'hyperparameters': [10000, 0.09]}
# input_data = [[0.077], [0.068], [0.092]]
input_data = 0.078
# Send an HTTP POST request to the API endpoint
response = requests.post('http://localhost:8080/stream', json={'data': input_data})
# response = requests.get('http://localhost:8080/log')

# Retrieve the inference result from the response
inference_result = response.json()['result']

# Print the inference result
print(inference_result)