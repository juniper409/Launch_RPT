import requests
import json

response = requests.get('https://lldev.thespacedevs.com/2.2.0/launch/upcoming/')

status = response.status_code
x = 0

#Gives error code if the connection fails.
if status != 200:
    print("Error retrieving data -", status)
else:
    pass

while x <= 10:
    #Retrieves the needed info from the API and assigns variable.
    name = response.json()['results'][x]['name']
    date = response.json()['results'][x]['net']
    location = response.json()['results'][x]['pad']['name']
    launch_description = response.json()['results'][x]['mission']['description']
    
    #Print Data
    print(f'----- {name} -----')
    print(f'Launch D&T: {date}')
    print(f'From: {location}')
    print()
    x += 1
    if x == 10:
        break
    
        