
# ----------------URL and imports-------------------------
import requests
import GET_requests
URL = 'http://localhost:8088/services/users/'
#---------------REQUESTS------------------------------------
def update_user(id, key, value):
    response_1 = GET_requests.get_user_by_id(id)
    #d  = {key : value}
    response_1[key] = value
    response = requests.put(URL + "updateUser/"
                            ,json=(response_1))
    print('PUT into the USER REQUEST----',response)
    return response
#-------------------------------------------------------------

