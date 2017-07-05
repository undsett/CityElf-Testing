import schedule
import time
import requests

def job():
    response = requests.get('http://localhost:8088/services/forecasts/startCollector')
    print("I'm working...", time.ctime(time.time()))
    #print(response.content) #uncomment in case of error to see error message
    print(response)
    return response

schedule.every(10).minutes.do(job)

if __name__ == '__main__':
    while 1:
        schedule.run_pending()
        time.sleep(60)
