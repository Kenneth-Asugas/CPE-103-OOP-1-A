import tkinter as tk
import math
import os

root = tk.Tk()
root.title("Advanced Calculator")
root.configure(bg="#2E3440")
root.resizable(False, False)

icon_path = "calc icon.ico"
if os.path.isfile(icon_path):
    root.iconbitmap(icon_path)
else:
    print(f"Error: Icon file '{icon_path}' not found. Current directory: {os.getcwd()}")

display = tk.Entry(root, font=('Arial', 20), bd=10, relief=tk.RIDGE,
                   bg="#D8DEE9", fg="#2E3440", justify="right")
display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipadx=20, ipady=10)

def click(symbol):
    display.insert(tk.END, symbol)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        expression = display.get()
        expression = expression.replace("÷", "/")
        expression = expression.replace("×", "*")
        expression = expression.replace("−", "-")
        expression = expression.replace("^", "**")
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def sin_func():
    try:
        angle = float(display.get())
        result = math.sin(math.radians(angle))
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def cos_func():
    try:
        angle = float(display.get())
        result = math.cos(math.radians(angle))
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def clear_from_menu(event=None):
    clear()

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=edit_menu)
edit_menu.add_command(label="Clear", command=clear_from_menu)

btn_font = ('Arial', 16, 'bold')
btn_bg_normal = "#ECEFF4"
btn_bg_operators = "#81A1C1"
btn_bg_equals = "#A3BE8C"
btn_bg_clear = "#BF616A"
btn_fg = "#2E3440"
btn_relief = tk.RAISED
btn_bd = 3

buttons = [
    ("C", 1, 0, 1), ("sin", 1, 1, 1), ("cos", 1, 2, 1), ("^", 1, 3, 1),
    ("7", 2, 0, 1), ("8", 2, 1, 1), ("9", 2, 2, 1), ("÷", 2, 3, 1),
    ("4", 3, 0, 1), ("5", 3, 1, 1), ("6", 3, 2, 1), ("×", 3, 3, 1),
    ("1", 4, 0, 1), ("2", 4, 1, 1), ("3", 4, 2, 1), ("−", 4, 3, 1),
    ("0", 5, 0, 2), (".", 5, 2, 1), ("+", 5, 3, 1),
    ("=", 6, 0, 4)
]

for (text, row, col, colspan) in buttons:
    if text == "C":
        cmd = clear
        bg_color = btn_bg_clear
    elif text == "=":
        cmd = calculate
        bg_color = btn_bg_equals
    elif text == "sin":
        cmd = sin_func
        bg_color = btn_bg_operators
    elif text == "cos":
        cmd = cos_func
        bg_color = btn_bg_operators
    elif text == "^":
        cmd = lambda: click("^")
        bg_color = btn_bg_operators
    elif text in ("÷", "×", "−", "+"):
        cmd = lambda t=text: click(t)
        bg_color = btn_bg_operators
    else:
        cmd = lambda t=text: click(t)
        bg_color = btn_bg_normal

    btn = tk.Button(root, text=text, font=btn_font, width=6, height=2,
                    relief=btn_relief, bd=btn_bd, bg=bg_color, fg=btn_fg,
                    activebackground="#4C566A", activeforeground="#ECEFF4",
                    command=cmd)
    btn.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2, sticky="nsew")

for i in range(5):
    root.grid_columnconfigure(i, weight=1)

root.bind("<Control-c>", clear_from_menu)

root.mainloop()
