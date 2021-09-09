import requests

URl = 'http://127.0.0.1:8000/stuinfo/1/'

response = requests.get(URl)

data = response.json()

print(data)