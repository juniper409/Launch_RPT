import datetime
import requests
import json

response = requests.get('https://lldev.thespacedevs.com/2.2.0/launch/upcoming/')
status = response.status_code
f = open("list.txt","a")

#Gives error code if the connection fails.
if status != 200:
    print("Error retrieving data -", status)
    f.write("Error retrieving data -", status)
else:
    pass
    x=0
while x <= 10:
    #Retrieves the needed info from the API and assigns variable.
    name = response.json()['results'][x]['name']
    date = response.json()['results'][x]['net']
    location = response.json()['results'][x]['pad']['name']
    launch_description = response.json()['results'][x]['mission']['description']
        
    #Print Data
    f.writelines(f'----- {name} -----\n')
    f.writelines(f'Launch D&T: {date}\n')
    f.writelines(f'From: {location}\n')
    f.write("\n")
    x += 1
    if x == 10:
        f.close()
        break
            
print("REPORT CREATION COMPLETE")
