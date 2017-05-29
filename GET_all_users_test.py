#---------------GET ALL USERS----------------------

#----------------URL and imports----------------------
import requests #Should be install requests libary
import unittest
URL = 'http://localhost:8088/services/users/'
#---------------REQUESTS--------------------------------
def get_users():
    response = requests.get(URL+'all')
    users = response.json()
    #print(response.content)            #In case of error u can remove '#' and see more delailed description
    return users
def get_users_response():
    response = requests.get(URL+'all')
    users = response.json()
    #print(response.content)            #In case of error u can remove '#' and see more delailed description
    return response
#-------------TEST RESPONSE AND DICT-----------------------
class TestIsReturnUsers(unittest.TestCase):
    def test_is_return_users(self):
        get_users_check = get_users()
        for dct in get_users_check:
            for key,value in dct.items():
                self.assertTrue(key == 'id')
                break
    def test_is_correct_response(self):
        r = (get_users_response())
        str_r = str(r)
        self.assertTrue(str_r == '<Response [200]>')
#--------------Main body------------------------------------------
if __name__ == '__main__':
    #print(get_users())               #Remove '#' to see all received users
    #print(get_users_response())      # Remove '#' to see response
    unittest.main()
#--------------------------------------------------------------------