import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
import os

window = tk.Tk()
window.title('Birth Date Selector')
window.geometry('500x250')

# Icon
icon_path = "1486051847-twitchsocialnetworkbrandlogo_79103.ico"
if os.path.isfile(icon_path):
    window.iconbitmap(icon_path)
else:
    print("Error: Icon file not found.")

for i in range(5):
    window.grid_rowconfigure(i, weight=1)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=2)

def show_birth_info():
    birth_month = month.get()
    birth_day = day.get()
    birth_year = year.get()
    showinfo(title="Birth Date Info", message=f'You selected: {birth_month} {birth_day}, {birth_year}')

def update_background(event=None):
    bg_path = "2022_Acer_Consumer_Option_04_3840x2400.jpg"
    try:
        if os.path.isfile(bg_path):
            bg_image = Image.open(bg_path)
            bg_image = bg_image.resize((window.winfo_width(), window.winfo_height()))
            bg_photo = ImageTk.PhotoImage(bg_image)
            bg_label.config(image=bg_photo)
            bg_label.image = bg_photo
        else:
            print("Error: Background image not found.")
    except Exception as e:
        print(f"Error loading background: {e}")

# Background
bg_label = tk.Label(window)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

window.bind("<Configure>", update_background)

# Title
title_label = ttk.Label(window, text="Select Your Birth Date", font=("Times New Roman", 18, 'bold'))
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Birth Month
month_label = ttk.Label(window, text="Birth Month:", font=("Times New Roman", 14))
month_label.grid(column=0, row=1, padx=10, pady=5, sticky="w")

month = ttk.Combobox(window, font=("Times New Roman", 14))
month['values'] = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
month.grid(column=1, row=1, padx=10, pady=5, sticky="nsew")
month.current(0)

# Birth Day
day_label = ttk.Label(window, text="Birth Day:", font=("Times New Roman", 14))
day_label.grid(column=0, row=2, padx=10, pady=5, sticky="w")

day = ttk.Combobox(window, font=("Times New Roman", 14))
day['values'] = tuple(str(i) for i in range(1, 32))
day.grid(column=1, row=2, padx=10, pady=5, sticky="nsew")
day.current(0)

# Birth Year
year_label = ttk.Label(window, text="Birth Year:", font=("Times New Roman", 14))
year_label.grid(column=0, row=3, padx=10, pady=5, sticky="w")

year = ttk.Combobox(window, font=("Times New Roman", 14))
year['values'] = tuple(str(i) for i in range(1900, 2026))
year.grid(column=1, row=3, padx=10, pady=5, sticky="nsew")
year.current(0)

# Submit Button
submit_button = ttk.Button(window, text="Submit", command=show_birth_info)
submit_button.grid(row=4, column=0, columnspan=2, pady=20, sticky="nsew")

update_background()

window.mainloop()