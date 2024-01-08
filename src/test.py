import tkinter, subprocess, os

def run_script(region):
    base_path = "./src"
    script_path = os.path.join(base_path, region, "__init__.py")
    subprocess.run(["python", script_path])

root = tkinter.Tk()

root.configure(bg='black')

label = tkinter.Label(root, text="Welcome to Climate Pylot\n Please select target region...", bg='black', fg='white')
label.pack()

menu = tkinter.Menu(root)
root.config(menu=menu)

region_menu = tkinter.Menu(menu)
menu.add_cascade(label="Regions", menu=region_menu)

region_menu.add_command(label="North America", command=lambda: run_script("north_america"))
region_menu.add_command(label="Europe", command=lambda: run_script("europe"))
region_menu.add_command(label="Asia", command=lambda: run_script("asia"))
region_menu.add_command(label="South America", command=lambda: run_script("south_america"))
region_menu.add_command(label="Oceania", command=lambda: run_script("oceania"))
region_menu.add_command(label="Africa", command=lambda: run_script("africa"))
region_menu.add_command(label="Antarctica", command=lambda: run_script("antarctica"))

root.mainloop()