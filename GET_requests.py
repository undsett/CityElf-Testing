
#----------------URL and imports-----------------------
import requests #Should be install requests libary
URL = 'http://localhost:8088/services/'
#---------------REQUESTS--------------------------------
def get_users():
    response = requests.get(URL+'users/all')
    users = response.json()
    #print(response.content)            #In case of error u can remove '#' and see more delailed description
    return users
def get_users_response():
    response = requests.get(URL+'users/all')
    users = response.json()
    #print(response.content)  #           #In case of error u can remove '#' and see more delailed description
    print('GET ALL USERS Request----',response)
    return response

def serach_by_email(email):
    get_all_users = get_users()
    for dic in get_all_users:
        for key, value in dic.items():
            if value == email:
                id = dic['id']
                return id

def search_all_water_forecast():
    response = requests.get(URL + '/waterforecast/all')
    water_forecast = response.json()
    print('GET Water Forecast Request----',response)
    #print(water_forecast) #Uncomment to see all water forecast list
    return response

#------------------------BY ID--------------------------------------------
def get_user_by_id(id):
    response = requests.get(URL + 'users/' + str(id))
    user = response.json()
    #print(response.content)              #In case of error u can remove '#' and see more delailed description
    print('GET user by ID rquest----',response)
    #print(user)
    return user

def get_notifications_by_id(id):
    response = requests.get(URL + '/notification/settings/' + str(id))
    user_notification = response.json()

    print('GET notifications by ID rquest----', response)
    return response,user_notification

#-------------------------------------------------------------
