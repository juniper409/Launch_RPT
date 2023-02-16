import datetime
import json
from time import time_ns
import requests
time_now = datetime.datetime.now()
#print(time_now.strftime('Today is %B %d, %Y'))
response = requests.get('https://lldev.thespacedevs.com/2.2.0/launch/upcoming/')

x=3

date = response.json()['results'][x]['net']

year = int(date[0:4])
month = int(date[5:7])
day = int(date[8:10])
hour = int(date[11:12])
min = int(date[14:15])

time = datetime.datetime(year, month, day)

print(time.strftime('%B %d, %Y at' ))
#print(time)