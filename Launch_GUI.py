import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("700x500")
root.title("Launch Report")

#Whole window frame
frame = tk.Frame(root)


#Generate Button
submit_button=tk.Button(root, text="Submit")
submit_button.grid(row=0, column=4)

#Exit Button
exit_button=tk.Button(root, text="EXIT")
exit_button.grid(row=4, column=3)

#Save Button
Export_button = tk.Button(root, text="EXPORT")
Export_button.grid(row=4, column=2)

#Company Drop Down Menu
company_menu = ttk.Combobox(root, values=["ALL","SpaceX", "ULA", "NASA", "RocketLab", "Something"])
company_menu.grid(row=0, column=0)


#Ends the program
root.mainloop()
