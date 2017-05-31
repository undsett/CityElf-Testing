#---------------TEST PUT Request------------------------

#----------------URL and imports-------------------------
import requests
import json
import unittest
URL = 'http://localhost:8088/services/users/'
#---------------REQUESTS-----------------------------------
def get_user_by_id(id):
    response = requests.get(URL + str(id))
    user = response.json()
    return user

def update_user(id, key, value):
    response_1 = get_user_by_id(id)
    #d  = {key : value}
    response_1[key] = value
    response = requests.put(URL + "updateUser/"
                            ,json=(response_1))
    print(response)
    return response

#---------------TEST_RESONSE--------------------------------
class TestResponse(unittest.TestCase):
    def test_response(self):
        str_r = str(r)
        self.assertTrue(str_r == '<Response [200]>')
#---------------MAIN BODY------------------------------------
if __name__ == '__main__':
    r = (update_user(42, 'firstname', 'Artem'))
    unittest.main()
#------------------------------------------------------------
