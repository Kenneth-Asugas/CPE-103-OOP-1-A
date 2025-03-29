from tkinter import *

window = Tk()
window.title("Using grid manager")
window.geometry("400x200")


yscroll=Scrollbar(window, orient=VERTICAL)
yscroll.pack(side=RIGHT, fill=Y)

lstbox = Listbox(window)
lstbox.pack(side=LEFT, fill=BOTH, expand=True)

for x in range(51):
    lstbox.insert(END,x)

lstbox.config(yscrollcommand=yscroll.set)
yscroll.config(command=lstbox.yview)

window.mainloop()