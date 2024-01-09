import tkinter

root = tkinter.Tk()

label = tkinter.Label(root, text="Welcome to Climate Pylot\n Please select target region...")
label.pack()

menu = tkinter.Menu(root)
root.config(menu=menu)

file_menu = tkinter.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)

region_menu = tkinter.Menu(menu)
menu.add_cascade(label="Regions", menu=region_menu)

def open_folder(region):
    import os
    import subprocess
    folder_path = os.path.join("./src", region)
    init_file_path = os.path.join(folder_path, "__init__.py")
    subprocess.run(["python", init_file_path])

region_menu.add_command(label="North America", command=lambda: open_folder("north_america"))
region_menu.add_command(label="Europe", command=lambda: open_folder("europe"))
region_menu.add_command(label="South America", command=lambda: open_folder("south_america"))
region_menu.add_command(label="Asia", command=lambda: open_folder("asia"))
region_menu.add_command(label="Africa", command=lambda: open_folder("africa"))
region_menu.add_command(label="Oceania", command=lambda: open_folder("oceania"))
region_menu.add_command(label="Antarctica", command=lambda: open_folder("antarctica"))

root.mainloop()