import requests
import Constants
import utils
import smtplib
import json
import time
import threading

cur = time.time()

SUBJECT = "covid vaccine is available : "

print(cur)


def kanpurChecker():
    print('Calling cowin service to fetch results')
    response = requests.get(utils.getFullUrl(Constants.DISTRICT_CODE_KANPUR), headers=Constants.headers)
    flag, resp = utils.process(response.json())

    if flag:
        print('Sending mail data')
        li = ["saurabh189956@gmail.com"]

        for dest in li:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("saurabh189956@gmail.com", "password to be placed here in plane text")  # sender email and password
            message = 'Subject: {}\n\n{}'.format(SUBJECT, json.dumps(resp))
            s.sendmail("saurabh189956@gmail.com", dest, message)
            s.quit()

    threading.Timer(Constants.INTERVAL, kanpurChecker).start()


def ahmedabadChecker():
    print('Calling cowin service to fetch results')
    response = requests.get(utils.getFullUrl(Constants.DISTRICT_CODE_AHM), headers=Constants.headers)
    flag, resp = utils.process(response.json())

    if flag:
        print('Sending mail data')
        li = ["vrushalipujara97@gmail.com"]

        for dest in li:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("saurabh189956@gmail.com", "password to be placed here in plane text")  # sender email and password
            message = 'Subject: {}\n\n{}'.format(SUBJECT, json.dumps(resp))
            s.sendmail("saurabh189956@gmail.com", dest, message)
            s.quit()

    threading.Timer(Constants.INTERVAL, ahmedabadChecker).start()


kanpurChecker()
ahmedabadChecker()
