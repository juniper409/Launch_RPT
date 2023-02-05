import requests
import json

response = requests.get('https://lldev.thespacedevs.com/2.2.0/launch/upcoming/')

number = input("List number: ")
number = int(number)

#Retrieves the needed info from the API and assigns variable.
name = response.json()['results'][number]['name']
date = response.json()['results'][number]['net']
location = response.json()['results'][number]['pad']['name']
launch_description = response.json()['results'][number]['mission']['description']
status = response.status_code

#Gives error code if the connection fails.
if status != 200:
    print("Error retrieving data -", status)
else:
    pass

#Print Data
print(f'----- {name} -----')
print(f'Launch Date & Time: {date}')
print(f'From: {location}')