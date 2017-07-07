import schedule
import time
import requests
import unittest

def job():
    response = requests.get('http://localhost:8088/services/forecasts/startCollector')
    print("I'm working...", time.ctime(time.time()))
    #print(response.content) #uncomment in case of error to see error message
    print(response)
    return response

class TestResponse(unittest.TestCase):
    def test_response(self):
        str_r = str(start)
        self.assertTrue(str_r == '<Response [200]>')


if __name__ == '__main__':
    start = schedule.every(1).minutes.do(job)
    while 1:
        schedule.run_pending()
        time.sleep(1)




'''import schedule
import time
import requests

def job():
    response = requests.get('http://localhost:8088/services/forecasts/startCollector')
    print("I'm working...", time.ctime(time.time()))
    print(response.content) #uncomment in case of error to see error message
    print(response)
    return response

schedule.every(1).minutes.do(job)

if __name__ == '__main__':
    while 1:
        schedule.run_pending()
        time.sleep(1)'''