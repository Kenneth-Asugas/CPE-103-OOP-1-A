import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.configure(bg="lightblue")
root.resizable(False, False)

display = tk.Entry(root, font=('Arial', 20), bd=10, relief=tk.RIDGE, bg="lightcyan", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=20, ipady=10)

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
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

btn_font = ('Arial', 16, 'bold')
btn_bg = 'whitesmoke'
btn_relief = tk.RAISED
btn_bd = 4

buttons = [
    ("C", 1, 0, 4),

    ("7", 2, 0, 1), ("8", 2, 1, 1), ("9", 2, 2, 1), ("÷", 2, 3, 1),
    ("4", 3, 0, 1), ("5", 3, 1, 1), ("6", 3, 2, 1), ("×", 3, 3, 1),
    ("1", 4, 0, 1), ("2", 4, 1, 1), ("3", 4, 2, 1), ("−", 4, 3, 1),
    ("0", 5, 0, 2), (".", 5, 2, 1), ("+", 5, 3, 1),
    ("=", 6, 0, 4)
]

for (text, row, col, colspan) in buttons:
    if text == "C":
        cmd = clear
    elif text == "=":
        cmd = calculate
    else:
        cmd = lambda t=text: click(t)

    btn = tk.Button(root, text=text, font=btn_font, width=6, height=2,
                    relief=btn_relief, bd=btn_bd, bg=btn_bg, command=cmd)
    btn.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2, sticky="nsew")

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
