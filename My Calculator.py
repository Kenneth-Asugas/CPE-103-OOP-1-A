from tkinter import *

class MyWindow:
    def __init__(self, win):
        win.configure(bg='orange')

        self.lbl1 = Label(win, text='First number', fg='white', bg='green')
        self.lbl2 = Label(win, text='Second number', fg='white', bg='green')
        self.lbl3 = Label(win, text='Result', fg='white', bg='green')

        self.t1 = Entry(bd=3, fg='green', bg='white')
        self.t2 = Entry(fg='green', bg='white')
        self.t3 = Entry(fg='green', bg='white')

        self.b1 = Button(win, text='Add', command=self.add, fg='white', bg='green')
        self.b2 = Button(win, text='Subtract', fg='white', bg='green')
        self.b3 = Button(win, text='Multiply', command=self.multiply, fg='white', bg='green')
        self.b4 = Button(win, text='Divide', command=self.divide, fg='white', bg='green')
        self.b5 = Button(win, text='Clear', command=self.clear, fg='white', bg='green')
        self.b2.bind('<Button-1>', self.sub)

        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b1.place(x=50, y=150)
        self.b2.place(x=125, y=150)
        self.b3.place(x=225, y=150)
        self.b4.place(x=325, y=150)
        self.b5.place(x=50, y=198)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)

    def add(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 + num2
        self.t3.insert(END, str(result))

    def sub(self, event):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 - num2
        self.t3.insert(END, str(result))

    def multiply(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 * num2
        self.t3.insert(END, str(result))

    def divide(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        if num2 == 0:
            result = "Error"
        else:
            result = num1 / num2
        self.t3.insert(END, str(result))

    def clear(self):
        self.t1.delete(0, 'end')
        self.t2.delete(0, 'end')
        self.t3.delete(0, 'end')

window = Tk()
mywin = MyWindow(window)
window.title('Calculator')
window.geometry("500x300+10+10")
window.mainloop()