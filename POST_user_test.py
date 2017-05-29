#-------------TEST POST USER----------------------------

#----------------URL and imports-------------------------
import requests
import json
import unittest
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
    print(response)
    return response
#--------------TEST response answer------------------------------------
class TestIsPosted(unittest.TestCase):
    def test_post_resonse(self):
        str_r = str(r)
        self.assertTrue(str_r == '<Response [200]>')
#-------------Main body-----------------------------------------------
if __name__ =='__main__':
    r = post_user(42, 'Andrew', 'Rozhko', 'Pishonovskaya 22', 'Rozhkoandrey@gmail.com', '0935549520', False, True,
                  False,
                  'Deribasovskaya 1', 'Gagarina 20')
    unittest.main()

