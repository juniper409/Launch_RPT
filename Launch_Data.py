import requests
import json

response = requests.get('https://lldev.thespacedevs.com/2.2.0/launch/upcoming/')

launch_name = response.json()['results'][0]['name']
launch_date = response.json()['results'][0]['net']
launch_description = response.json()['results'][0]['mission']['description']




if response.status_code == 200:
    print("Connection Successful!")
else:
    print("Error: There was a problem connecting.")

print(f'{launch_name}')
print(f'Launch Date & Time: {launch_date}')
