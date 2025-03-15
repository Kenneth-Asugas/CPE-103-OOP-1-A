#GUI Conversion of the Calculator:
import tkinter as tk
from tkinter import messagebox
import math

# Functions for calculation
def validate_input(entry):
    try:
        return float(entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number")
        return None

def add():
    num1, num2 = validate_input(entry1), validate_input(entry2)
    if num1 is not None and num2 is not None:
        res = num1 + num2
        result.set(res)
        add_history(f"{num1} + {num2} = {res}")

def subtract():
    num1, num2 = validate_input(entry1), validate_input(entry2)
    if num1 is not None and num2 is not None:
        res = num1 - num2
        result.set(res)
        add_history(f"{num1} - {num2} = {res}")

def multiply():
    num1, num2 = validate_input(entry1), validate_input(entry2)
    if num1 is not None and num2 is not None:
        res = num1 * num2
        result.set(res)
        add_history(f"{num1} × {num2} = {res}")

def divide():
    num1, num2 = validate_input(entry1), validate_input(entry2)
    if num1 is not None and num2 is not None:
        if num2 == 0:
            result.set("Error! Division by zero.")
        else:
            res = num1 / num2
            result.set(res)
            add_history(f"{num1} ÷ {num2} = {res}")

def square_root():
    num = validate_input(entry1)
    if num is not None:
        if num < 0:
            result.set("Error! Negative root.")
        else:
            res = math.sqrt(num)
            result.set(res)
            add_history(f"√{num} = {res}")

def cube_root():
    num = validate_input(entry1)
    if num is not None:
        res = num ** (1/3)
        result.set(res)
        add_history(f"³√{num} = {res}")

def power():
    num1, num2 = validate_input(entry1), validate_input(entry2)
    if num1 is not None and num2 is not None:
        res = num1 ** num2
        result.set(res)
        add_history(f"{num1} ^ {num2} = {res}")

def sin():
    num = validate_input(entry1)
    if num is not None:
        res = math.sin(math.radians(num))
        result.set(res)
        add_history(f"sin({num}°) = {res}")

def cos():
    num = validate_input(entry1)
    if num is not None:
        res = math.cos(math.radians(num))
        result.set(res)
        add_history(f"cos({num}°) = {res}")

def tan():
    num = validate_input(entry1)
    if num is not None:
        if (num % 90 == 0) and ((num // 90) % 2 != 0):  # Undefined at odd multiples of 90°
            result.set("Undefined")
        else:
            res = math.tan(math.radians(num))
            result.set(res)
            add_history(f"tan({num}°) = {res}")

def add_history(entry):
    history_list.insert(tk.END, entry)

def clear():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    result.set("")

def clear_history():
    history_list.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="gray")

# Create StringVar to hold the result
result = tk.StringVar()

button_style = {"font": ("Arial", 12), "width": 12, "height": 1}

# Create the layout
tk.Label(root, text="Enter first number:", font=("Arial", 14), bg="gray").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter second number:", font=("Arial", 14), bg="#f2f2f2").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Buttons for operations
tk.Button(root, text="+", command=add, fg='white', bg='dim gray', **button_style).grid(row=2, column=0)
tk.Button(root, text="−", command=subtract, fg='white', bg='dim gray', **button_style).grid(row=2, column=1)
tk.Button(root, text="×", command=multiply, fg='white', bg='dim gray', **button_style).grid(row=3, column=0)
tk.Button(root, text="÷", command=divide, fg='white', bg='dim gray', **button_style).grid(row=3, column=1)
tk.Button(root, text="a^b", command=power, fg='white', bg='dim gray', **button_style).grid(row=4, column=0)
tk.Button(root, text="√a", command=square_root, fg='white', bg='dim gray', **button_style).grid(row=4, column=1)
tk.Button(root, text="∛", command=cube_root, fg='white', bg='dim gray', **button_style).grid(row=5, column=0)
tk.Button(root, text="sin", command=sin, fg='white', bg='dim gray', **button_style).grid(row=5, column=1)
tk.Button(root, text="cos", command=cos, fg='white', bg='dim gray', **button_style).grid(row=6, column=0)
tk.Button(root, text="tan", command=tan, fg='white', bg='dim gray', **button_style).grid(row=6, column=1)
tk.Button(root, text="Clear", command=clear, fg='white', bg='green', **button_style).grid(row=7, column=0)
tk.Button(root, text="Clear History", command=clear_history, fg='white', bg='green', **button_style).grid(row=7, column=1)

# Label to show result
tk.Label(root, text="Result:", font=("Arial", 12), bg="white").grid(row=8, column=0)
result_label = tk.Label(root, textvariable=result, font=("Arial", 14), bg="light green", width=20, height=2)
result_label.grid(row=8, column=1)
tk.Label(root, text="History:", font=("Arial", 12), bg="white").grid(row=14, column=0)
history_list = tk.Listbox(root, height=6, width=40)
history_list.grid(row=15, column=0, columnspan=2)

# Start the main loop
root.mainloop()