import os

path = "/Users/chris/Desktop/list.txt"
file_check = os.path.exists(path)

if file_check == False:
    print("There is no file to write to. Please create the text file using this directory:\n"+ path)
    exit
else:
    print("Your file... it does exist! Continuing...")
    pass