import datetime
import requests
import json
import os

response = requests.get('https://lldev.thespacedevs.com/2.2.0/launch/upcoming/')
status = response.status_code
path = "/Users/chris/Desktop/list.txt"
f = open(path,"a")

#Gives error code if the connection fails.
if status != 200:
    print("Error retrieving data -", status)
    f.write("Error retrieving data -", status)
else:
    pass
x=0

#Check if .txt file is available for writing.
file_check = os.path.exists(path)

while file_check == False:
    print("There is no file to write to. Please create the text file using this directory:\n"+ path)
    break
else:
    print("Your file... it does exist! Continuing...")
    pass

#Runs while loop and adds 1 to the value of x to move to the next item in the library and lists the first ten items in the library.
while x <= 10:
    #Retrieves the needed info from the API and assigns variable.
    name = response.json()['results'][x]['name']
    launch_dt = response.json()['results'][x]['net']
    location = response.json()['results'][x]['pad']['name']
    launch_description = response.json()['results'][x]['mission']['description']
    year = int(launch_dt[0:4])
    month = int(launch_dt[5:7])
    day = int(launch_dt[8:10])
    hour = int(launch_dt[12:13])
    minute = int(launch_dt[15:16])
    second = int(launch_dt[18:19])
    date_form = datetime.datetime(year, month, day)
    time_form = datetime.time(hour, minute, second)
    ldate = date_form.strftime('%B %d,%Y')
    ltime = time_form
    
   
    #Print Data
    f.write(f'----- {name} -----\n')
    f.write(f'Launch D&T: {ldate} @ {ltime} UTC\n')
    f.write(f'From: {location}\n')
    f.write("\n")
    x += 1
    if x == 10:
        f.close()
        break
#if file_check == True:
    #print("REPORT CREATION COMPLETE")