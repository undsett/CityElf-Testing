
#----------------URL and imports----------------------
import requests #Should be install requests libary
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
#--------------------------------------------------------------------