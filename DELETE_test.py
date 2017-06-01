
#----------------URL and imports--------------------------
import requests             #Should be install requests libary
URL = 'http://localhost:8088/services/users/'
#---------------REQUESTS-----------------------------------
def delete_user_by_id(id):
    response = requests.delete(URL + str(id))
    print(response)
    return response
#------------------------------------------------------------