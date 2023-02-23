import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("700x500")
root.title("Launch Report")

#Generate Button
submit_button=tk.Button(root, text="Submit")
submit_button.pack()

#Exit Button
exit_button=tk.Button(root, text="EXIT")
exit_button.pack()

#Save Button
Export_button = tk.Button(root, text="EXPORT")
Export_button.pack()

#Company Drop Down Menu
company_menu = ttk.Combobox(root, values=["ALL","SpaceX", "ULA", "NASA", "RocketLab", "Something"])
company_menu.pack()

#Frames
top_frame = tk.Frame(root)
middle_frame_1 = tk.Frame(root)
middle_frame_1 = tk.Frame(root)
bottom_frame = tk.Frame(root)
root.mainloop()
