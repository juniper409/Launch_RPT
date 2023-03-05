import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

root = tk.Tk()
root.geometry("700x400")
root.title("Launch Report")

#Whole window frame
frame = ttk.Frame(root)

#Top Frame
select_frame = ttk.Frame(root)
select_frame.pack(side="top")

#Bottom Frame
bottom_frame = ttk.Frame(root)
bottom_frame.pack(side="bottom")

#Generate Button
submit_button=ttk.Button(select_frame, text="Submit")
submit_button.grid(row=0, column=1)

#Exit Button
exit_button=ttk.Button(bottom_frame, text="EXIT")
exit_button.grid(row=3, column =1)

#Export Button
export_button=ttk.Button(bottom_frame, text="Export")
export_button.grid(row=3, column=0)

#Company Drop Down Menu
company_menu = ttk.Combobox(select_frame, values=["ALL","SpaceX", "ULA", "NASA", "RocketLab", "Astra", "Firefly", "Blue Origin", "Relitivity Space","Northrop Grumman"])
company_menu.grid(row=0, column=0)

#Mid Frame (Content)
mid_frame = ttk.Frame(root)
mid_frame.pack(side="top")

#Content Area
content_area = scrolledtext.ScrolledText(mid_frame, height=20, width=90, padx=2, pady=2)
content_area.grid(row=3, column=1)



#Ends the program
root.mainloop()
