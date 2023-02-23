"""
This program prints out upcoming launches through the terminal with the option to print to a text file.

"""
import requests, datetime, os
from rich.table import Table
from rich.console import Console
x=0
response = requests.get('https://lldev.thespacedevs.com/2.2.0/launch/upcoming/')
console = Console()

#Clear console before execution.
os.system('cls' if os.name == 'nt' else 'clear')


#Create Columns in the table.
table = Table(title='Launch Schedule')
table.add_column("Launch", justify="left", style="blue", no_wrap="False")
table.add_column("Location", justify="left", style="blue", no_wrap="False")
table.add_column("Date/Time", justify="left", style="blue", no_wrap="False")
table.add_column("Status", justify="left", style="blue", no_wrap="False")

#Rows of the table
while x <= 10:
    #Retrieves the needed info from the API and assigns variable.
    name = response.json()['results'][x]['name']
    launch_dt = response.json()['results'][x]['net']
    location = response.json()['results'][x]['pad']['name']
    #launch_description = response.json()['results'][x]['mission']['description']
    year = int(launch_dt[0:4])
    month = int(launch_dt[5:7])
    day = int(launch_dt[8:10])
    hour = int(launch_dt[12:13])
    minute = int(launch_dt[15:16])
    second = int(launch_dt[18:19])
    date_form = datetime.datetime(year, month, day)
    time_form = datetime.time(hour, minute, second)
    ldate = date_form.strftime('%B %d,%Y')
    ltime = str(time_form)
    dt_combined = ldate +' @ '+ ltime + ' UTC'
    table.add_row(name, location, dt_combined, 'GO')
    x+=1  
    if x==10:
        break

console.print(table)