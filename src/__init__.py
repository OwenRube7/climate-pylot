"""
import tkinter

root = tkinter.Tk()

root.configure(bg='black')

label = tkinter.Label(root, text="Welcome to Climate Pylot\n Please select target region...", bg='black', fg='white')
label.pack()

menu = tkinter.Menu(root)
root.config(menu=menu)

region_menu = tkinter.Menu(menu)
menu.add_cascade(label="Regions", menu=region_menu)

region_menu.add_command(label="North America", command=lambda: open_folder("north_america))
region_menu.add_command(label="Europe", command=lambda: open_folder("europe"))
region_menu.add_command(label="South America", command=lambda: open_folder("south_america"))
region_menu.add_command(label="Asia", command=lambda: open_folder("asia"))
region_menu.add_command(label="Africa", command=lambda: open_folder("africa"))
region_menu.add_command(label="Oceania", command=lambda: open_folder("oceania"))
region_menu.add_command(label="Antarctica", command=lambda: open_folder("antarctica))

root.mainloop()
"""