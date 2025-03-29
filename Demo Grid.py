from tkinter import *

window = Tk()
window.title("Using grid manager")
window.geometry("400x250")

txtfld1 = Entry(window, bd=5, justify="center")
txtfld1.grid(row=0, column=0)
txtfld1.insert(END, "row 0, column 0")

txtfld2 = Entry(window, bd=5, justify="center")
txtfld2.grid(row=0, column=1)
txtfld2.insert(END, "row 0, column 1")

txtfld3 = Entry(window, bd=5, justify="center")
txtfld3.grid(row=0, column=2)
txtfld3.insert(END, "row 0, column 2")

txtfld4 = Entry(window, bd=5, justify="center")
txtfld4.grid(row=1, column=0)
txtfld4.insert(END, "row 1, column 0")

txtfld5 = Entry(window, bd=5, justify="center")
txtfld5.grid(row=1, column=1)
txtfld5.insert(END, "row 1, column 1")

txtfld6 = Entry(window, bd=5, justify="center")
txtfld6.grid(row=1, column=2)
txtfld6.insert(END, "row 1, column 2")

yscroll=Scrollbar(window, orient=VERTICAL)
yscroll.grid(row=3, column=2, sticky="nsw")

lstbox = Listbox(window)
lstbox.grid(row=3, column=1)

for x in range(51):
    lstbox.insert(END,x)

lstbox.config(yscrollcommand=yscroll.set)
yscroll.config(command=lstbox.yview)

window.mainloop()