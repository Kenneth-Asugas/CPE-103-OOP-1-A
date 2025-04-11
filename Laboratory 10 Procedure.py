import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo

window = tk.Tk()
window.title('Combobox')
window.geometry('500x250')  

def choice(event):
    month = event.widget.get()
    print("Your birth month", month)

ttk.Label(window, text="Choose your birth month",
          background='light yellow', foreground="black",
          font=("Times New Roman", 15)).grid(row=0, column=1)

ttk.Label(window, text="Select the month of your birth :",
          font=("Times New Roman", 12)).grid(column=0, row=5, padx=5, pady=25)

n = tk.StringVar()
month = ttk.Combobox(window, width=27, textvariable=n)

month['values'] = (' January',
                   ' February',
                   ' March',
                   ' April',
                   ' May',
                   ' June',
                   ' July',
                   ' August',
                   ' September',
                   ' October',
                   ' November',
                   ' December')

month.grid(column=1, row=5)
month.current(0)

def choice(event):
    showinfo(
        title="Selection",
        message=f'You selected {month.get()}'
    )
# Bind event for selection
month.bind("<<ComboboxSelected>>", choice)

# Run the main loop
window.mainloop()
