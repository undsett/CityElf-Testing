#----------------URL and imports-------------------------
import requests
import json
URL = 'http://localhost:8088/services/users/'
#---------------REQUESTS-----------------------------------

def post_user(id,firstname,lastname,address,email,phone,sms,email_not,push,recent_addresses,recent_addresses_2):
    user = {}
    user['id'] = id
    user['firstname'] = firstname
    user['lastname'] = lastname
    user['address'] = address
    user['email'] = email
    user['phone'] = phone
    notification = user['notification'] = {}
    notification['sms'] = sms
    notification['email'] = email_not
    notification['push'] = push
    recent_addresse = user['recentAddresses'] = []
    recent_addresse.append(recent_addresses)
    recent_addresse.append(recent_addresses_2)
    json_objct = json.dumps(user)
    response = requests.post(URL + 'addUser' , json=(user))
    print('POST request----',response)
    return response