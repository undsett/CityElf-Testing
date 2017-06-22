
#----------------URL and imports--------------------------
import requests             #Should be install requests libary
URL = 'http://localhost:8088/services/users/'
#---------------REQUESTS-----------------------------------
def delete_user_by_id(id):
    response = requests.delete(URL + str(id))
    print('DELETE request----',response)
    return response
#--------------------------------------------------------------
def get_user_by_id(id):
    response = requests.get(URL + str(id))
    user = response.json()
    #print(response.content)              #In case of error u can remove '#' and see more delailed description
    return user


