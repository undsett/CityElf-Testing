
#----------------URL and imports------------------
import requests #Should be install requests libary
URL = 'http://localhost:8088/services/users/recentAddresses/'
#---------------REQUESTS--------------------------
def get_adresses_by_id(id):
    response = requests.get(URL + str(id))
    adresses =  response.json()
    print(response)
    #print(response.content)            #In case of error u can remove '#' and see more delailed description
    return adresses

#-------------------------------------------------------------------