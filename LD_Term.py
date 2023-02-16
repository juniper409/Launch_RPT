import Launch_Data
from rich.table import Table
from rich.console import Console

row_num = 1
name = str(Launch_Data.name)
date = str(Launch_Data.ldate)
time = str(Launch_Data.ltime)
location = str(Launch_Data.location)


"""
This program prints out upcoming launches through the terminal with the option to print to a text file.

"""
#Create Columns in the table.
table = Table(title='Launch Schedule')
table.add_column("Launch", justify="center", style="blue", no_wrap="False")
table.add_column("Location", justify="center", style="blue", no_wrap="False")
table.add_column("Date/Time", justify="center", style="blue", no_wrap="False")
table.add_column("Status", justify="center", style="blue", no_wrap="False")

#Rows of the table
table.add_row(name, location, date + time, 'GO')


console = Console()
console.print(table)