import requests


# Define the input data

input_data_batch = [[0.077], [0.068], [0.092]]
input_data_stream = 0.078
# Send an HTTP POST request to the API endpoint
# response = requests.get('http://3.106.53.174:8080/log')
# response = requests.post('http://3.106.53.174:8080/batch', json={'data': input_data_batch})
response = requests.post('http://3.106.53.174:8080/stream', json={'data': input_data_stream})


# Retrieve the inference result from the response
inference_result = response.json()['result']
print(inference_result)