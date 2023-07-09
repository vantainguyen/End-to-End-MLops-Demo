import requests


demand = 'log' # 'batch', 'stream', 'log'
# Request invocation
if demand == 'batch':
    input_data_batch = [[0.077], [0.068], [0.092]]
    response = requests.post('http://3.106.53.174:8080/batch', json={'data': input_data_batch})
elif demand == 'stream':
    input_data_stream = 0.078
    response = requests.post('http://3.106.53.174:8080/stream', json={'data': input_data_stream})
elif demand == 'log':
    response = requests.get('http://3.106.53.174:8080/log')

# Retrieve the inference result from the response
inference_result = response.json()['result']
print(inference_result)