#----------------URL and imports-------------------------
import requests
import json
URL = 'http://localhost:8088/services/users/'
#---------------REQUESTS-----------------------------------

def post_user(email,phone,password):
    user = {}
    user['email'] = email
    user['phone'] = phone
    user['address'] = password
    #json_objct = json.dumps(user)
    response = requests.post(URL + 'addUser' , json=(user))
    print('POST request----',response)
    return response