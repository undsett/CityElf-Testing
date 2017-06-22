#----------------URL and imports-----------------------------
import requests
import json
URL = 'http://localhost:8088/services/'
#---------------REQUESTS--------------------------------------

def post_user(email,phone,password):
    user = {}
    user['email'] = email
    user['phone'] = phone
    user['address'] = password
    #json_objct = json.dumps(user)
    response = requests.post(URL + 'users/addUser' , json=(user))
    print('POST request----',response)
    return response

def post_for_forgot_password(email):
    response = requests.post(URL + 'forgot/reset?email=' + str(email))
    print('FORGOT password response -----',response)
    print(response.links)
    return response

'''def test_post():
    response = requests.post('http://localhost:8088/services/forgot/
        newPassword?token= ***ENTER YOUR TOKEN HERE*** &newPassword= ***ENTER YOUR NEW PASSWORD HERE ***')
    print(response)
    print(response.content)
    return response

if __name__ == '__main__':
    test_post()
#-----------------------------------------------------------------'''