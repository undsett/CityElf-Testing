#----------------GET BY ID TEST--------------------------

#----------------URL and imports-------------------------
import requests #Should be install requests libary
import unittest

URL = 'http://localhost:8088/services/users/'
#---------------REQUESTS-----------------------------------
def get_user_by_id(id):
    response = requests.get(URL + str(id))
    user = response.json()
    #print(response.content)              #In case of error u can remove '#' and see more delailed description
    #print(response)
    return user
#------------Test is requested ID in the DICT---------------
class TestIsReturnUserById(unittest.TestCase):
    def test_is_correct_id(self):
        user_id = get_user_by_id(42)['id']
        self.assertEqual(user_id,42)
    def test_is_corect_name(self):
        self.assertEqual(get_user_by_id(42)['firstname'],'Artem')
    def test_is_correct_lastname(self):
        self.assertEqual(get_user_by_id(42)['lastname'], 'Rozhko')
    def test_is_correct_email(self):
        self.assertEqual(get_user_by_id(42)['email'], 'Rozhkoandrey@gmail.com')

#------------Main body--------------------------------------
if __name__=='__main__':
    unittest.main()
#------------------------------------------------------------
