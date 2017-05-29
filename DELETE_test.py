#----------------DELETE TEST------------------------------

#----------------URL and imports--------------------------
import requests             #Should be install requests libary
import unittest

URL = 'http://localhost:8088/services/users/'
#---------------REQUESTS-----------------------------------
def get_user_by_id(id):
    response = requests.get(URL + str(id))
    user = response.json()
    return user

def delete_user_by_id(id):
    response = requests.delete(URL + str(id))
    print(response)
    return response
#--------------TEST IS USER DELETED BY ID------------------
class TestIsUserDeleted(unittest.TestCase):
    def test_is_user_deleted(self):
        self.assertEqual(get_user_by_id(user_id)['status'],404)
    def test_delete_response(self):
        str_r = str(r)
        self.assertTrue(str_r == '<Response [200]>')
#--------------Main body--------------------------------------
if __name__=='__main__':
    user_id = 42              #put here userId which you want to deleate and test
    r = delete_user_by_id(user_id)
    unittest.main()
#------------------------------------------------------------