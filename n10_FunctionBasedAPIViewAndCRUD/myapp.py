import requests
from json import dumps

URL = 'http://127.0.0.1:8000/studentapi/'

print('1 :- Show Data ')
print('2 :- Post Data ')
print('3 :- Update Data ')
print('4 :- Delete Data ')
print('0 :- Exit')

i = int(input('Select :-'))
if i != 0:
    if i == 1:
        def get_data(id = None ):
            data = {}
            if id is not None:
                data = {'id':id}    
            headers = {'content-Type':'application/json'}
            json_data = dumps(data)
            response = requests.get(url = URL, headers = headers ,data = json_data)
            data = response.json()
            print(data) 

        get_data(1)

    elif i == 2:

        def post_data():
            print('++++++++++++ Enter Data +++++++++++')
            name = input("Enter the name of student:")
            roll = int(input("Enter the roll number of student:"))
            city = input("Enter the city of student:")

            data = {
                'name':name,
                'roll':roll,
                'city':city,
            }
            headers = {'content-Type':'application/json'}

            json_data = dumps(data)
            response = requests.post(url = URL, headers = headers , data = json_data)
            data = response.json()
            print(data)

        post_data()

    elif i == 3:
        def update_data():
            
            print('++++++++++++ Enter Id For Update Data+++++++++++')
            id = int(input("Enter a id of student:"))
            data = {
                'id': id,
                'name':'Jaineel',
                'city':'Ahm',
            }
            headers = {'content-Type':'application/json'}
            json_data = dumps(data)
            response = requests.put(url = URL,headers = headers , data = json_data)
            data = response.json()
            print(data)

        update_data()

    elif i == 4:
        def delete_data():
            print('++++++++++++ Enter Id For Delete Data+++++++++++')
            id = int(input("Enter a id of student:"))

            data = {
                'id': id,
            }
            headers = {'content-Type':'application/json'}
            json_data = dumps(data)
            response = requests.delete(url = URL, headers = headers ,data = json_data)
            data = response.json()
            print(data)

        delete_data()