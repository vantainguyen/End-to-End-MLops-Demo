import requests

def test_integration():
    assert 0 == 0

# demand = 'batch' # 'batch', 'stream', 'log', 'emptyLog
# # Request invocation
# if demand == 'batch':
#     input_data_batch = [[0.077], [0.068], [0.092]]
#     response = requests.post('http://13.239.25.119:8080/batch', json={'data': input_data_batch})
# elif demand == 'stream':
#     input_data_stream = 0.077
#     response = requests.post('http://13.239.25.119:8080/stream', json={'data': input_data_stream})
# elif demand == 'log':
#     response = requests.get('http://13.239.25.119:8080/log')
# elif demand == 'emptyLog':
#     response = requests.get('http://13.239.25.119:8080/emptyLog')

# # Retrieve the inference result from the response
# inference_result = response.json()['result']
# print(inference_result)
