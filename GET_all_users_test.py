
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
    #print(response.content)  #           #In case of error u can remove '#' and see more delailed description
    print('GET ALL Request----',response)
    return response

def serach_by_email(email):
    get_all_users = get_users()
    for dic in get_all_users:
        for key, value in dic.items():
            if value == email:
                id = dic['id']
                return id
#---------------------------------------------------------------------