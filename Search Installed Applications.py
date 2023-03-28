from tkinter import *
import winapps
def app():
	for item in winapps.search_installed(e.get()):
		name.set(item.name)
		version.set(item.version)
		Install_date.set(item.install_date)
		publisher.set(item.publisher)
		uninstall_string.set(item.uninstall_string)
master = Tk()
master.title("Installed Apps Info")
master.configure(bg='light grey')
name = StringVar()
version = StringVar()
Install_date = StringVar()
publisher = StringVar()
uninstall_string = StringVar()
Label(master, text="Enter app name:",
	bg="light grey").grid(row=0, sticky=W)
Label(master, text="Name: ",
	bg="light grey").grid(row=2, sticky=W)
Label(master, text="Version:",
	bg="light grey").grid(row=3, sticky=W)
Label(master, text="Installation date:",
	bg="light grey").grid(row=4, sticky=W)
Label(master, text="Publisher:",
	bg="light grey").grid(row=5, sticky=W)
Label(master, text="Uninstall string:",
	bg="light grey").grid(row=6, sticky=W)
Label(master, text="", textvariable=name,
	bg="light grey").grid(row=2, column=1, sticky=W)
Label(master, text="", textvariable=version,
	bg="light grey").grid(row=3, column=1, sticky=W)
Label(master, text="", textvariable=Install_date,
	bg="light grey").grid(row=4, column=1, sticky=W)
Label(master, text="", textvariable=publisher,
	bg="light grey").grid(row=5, column=1, sticky=W)
Label(master, text="", textvariable=uninstall_string,
	bg="light grey").grid(row=6, column=1, sticky=W)
e = Entry(master, width=30)
e.grid(row=0, column=1)
b = Button(master, text="View Info", command=app, bg="Red")
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5,)
mainloop()
