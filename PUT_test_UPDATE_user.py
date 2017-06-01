import GET_user_by_id_test
#----------------URL and imports-------------------------
import requests
import json
URL = 'http://localhost:8088/services/users/'
#---------------REQUESTS-----------------------------------
def update_user(id, key, value):
    response_1 = GET_user_by_id_test.get_user_by_id(id)
    #d  = {key : value}
    response_1[key] = value
    response = requests.put(URL + "updateUser/"
                            ,json=(response_1))
    print(response)
    return response
#-----------------------------------------------------------

