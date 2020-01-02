from tkinter import *

root = Tk()
root.title("Simple calculator")

e = Entry(root, width=20, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# functions

def button_click(number):
    num = e.get()
    e.delete(0, END)
    e.insert(0, str(num) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    global num1
    global math
    num1 = int(e.get())
    math = "addition"
    e.delete(0, END)

def button_subs():
    global num1
    global math
    num1 = int(e.get())
    math = "substraction"
    e.delete(0, END)

def button_divide():
    global num1
    global math
    num1 = int(e.get())
    math = "divition"
    e.delete(0, END)

def button_multy():
    global num1
    global math
    num1 = int(e.get())
    math = "multiplication"
    e.delete(0, END)


def button_result():
    num2 = int(e.get())
    e.delete(0, END)

    if math == "addition":
        e.insert(0, num1 + num2)

    if math == "substraction":
        e.insert(0, num1 - num2)

    if math == "multiplication":
        e.insert(0, num1 * num2)

    if math == "divition":
        e.insert(0, num1 / num2)


# buttons grid

button_1 = Button(root, text="1", padx=20, pady=10, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=20, pady=10, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=20, pady=10, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=20, pady=10, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=20, pady=10, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=20, pady=10, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=20, pady=10, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=20, pady=10, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=20, pady=10, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=47, pady=10, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=20, pady=31.5, command=button_add)
button_subs = Button(root, text="-", padx=22, pady=10, command=button_subs)
button_multy = Button(root, text="x", padx=20, pady=10, command=button_multy)
button_divide = Button(root, text="/", padx=22, pady=10, command=button_divide)
button_result = Button(root, text="=", padx=20, pady=31.5, command=button_result)
button_clear = Button(root, text="Clear", padx=40, pady=10, command=button_clear)

# button grid
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=0, columnspan=2)
button_clear.grid(row=5, column=2, columnspan=2)


button_subs.grid(row=1, column=2)
button_multy.grid(row=1, column=1)
button_divide.grid(row=1, column=0)

button_add.grid(row=1, column=3, rowspan=2)
button_result.grid(row=3, column=3, rowspan=2)





root.mainloop()
