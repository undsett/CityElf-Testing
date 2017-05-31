#-------------Test GET ADRESSES-------------------

#----------------URL and imports------------------
import requests #Should be install requests libary
import unittest
URL = 'http://localhost:8088/services/users/recentAddresses/'
#---------------REQUESTS--------------------------
def get_adresses_by_id(id):
    response = requests.get(URL + str(id))
    adresses =  response.json()
    print(response)
    #print(response.content)            #In case of error u can remove '#' and see more delailed description
    return adresses
#-------------TEST is return any list--------------
class Test_is_return_adresses(unittest.TestCase):
    def test_is_return_something(self):
        self.assertEqual(type(get_adresses_by_id(42)),type([]))

    def test_is_correct_address(self):
        get_adresses_check = get_adresses_by_id(42)
        self.assertEqual(get_adresses_check[0],'Deribasovskaya 1',)
        self.assertEqual(get_adresses_check[1] ,'Gagarina 20')


#--------------Main body------------------------------------------
if __name__=='__main__':
    unittest.main()
#------------------------------------------------------------------