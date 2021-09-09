import requests
from json import dumps

URL = 'http://127.0.0.1:8000/studentapi/'

print('1 :- Show Data ')
print('2 :- Post Data ')

i = int(input('Select :-'))
if i != 0:
    if i == 1:
        def get_data(id =None ):
            data = {}
            if id is not None:
                data = {'id':id}    
            json_data = dumps(data)
            response = requests.get(url = URL, data = json_data)
            data = response.json()
            print(data)

        get_data()

    elif i == 2:

        def post_data():
            print('++++++++++++ Enter Data +++++++++++')
            name = input("Enter the name of student:")
            roll = int(input("Enter the roll number of student:"))
            email = input("Enter the Email of student:")

            data = {
                'name':name,
                'roll':roll,
                'email':email,
            }

            json_data = dumps(data)
            response = requests.post(url = URL, data = json_data)
            data = response.json()
            print(data)

        post_data()

