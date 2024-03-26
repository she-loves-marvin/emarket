#this is an example in python of how the fornt end people are expected to access the backend. through api requests

import requests

response = requests.get('http://127.0.0.1:8000/drinks')
print(response.json())