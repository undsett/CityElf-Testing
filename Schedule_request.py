import schedule
import time
import requests
import smtplib
from requests.auth import HTTPBasicAuth

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login("cityelfparsses@gmail.com", 'PASSWORD')  # BEFORE START SCRIPT ASK ME ABOUT PASSWORD

    msg = "Somethink wrong with PARSES work. Please check it!"
    server.sendmail("cityelfparsses@gmail", "cityelfodessa@gmail.com", msg)
    server.quit()

def job():
    response = requests.get('http://localhost:8088/services/forecasts/startcollector', auth=HTTPBasicAuth('SYSTEM','1234567890'))
    print("I'm working...", time.ctime(time.time()))
    #print(response.content) #uncomment in case of error to see error message
    print(response)
    if  str(response) != '<Response [200]>':
        send_email()
        print("Somethink wrong, email already send")
        print(response)
        print(response.content)
        #exit() # Uncomment to autocanceling script in case of fail
    return response


if __name__ == '__main__':
    start = schedule.every(1).minutes.do(job)

    while 1:
        schedule.run_pending()
        time.sleep(1)






