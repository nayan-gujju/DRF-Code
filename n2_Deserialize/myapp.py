import requests
from json import dumps
URl = 'http://127.0.0.1:8000/stucreate/'

data = {
    'name':'meet',
    'roll':103,
    'city':'Surat',
}

json_data = dumps(data)

response = requests.post(url=URl, data=json_data)

data = response.json()

print(data)