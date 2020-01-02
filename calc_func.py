# getting rid of bind and event
# using grid
# continuation from test_tk2.py

from tkinter import *


def sum():
    num1 = int(get_num1.get())
    num2 = int(get_num2.get())

    sum = num1 + num2
    resultbox.delete(0, "end")
    resultbox.insert(0, sum)

def minus():
    num1 = int(get_num1.get())
    num2 = int(get_num2.get())

    minus = num1 - num2
    resultbox.delete(0, "end")
    resultbox.insert(0, minus)

def multy():
    num1 = int(get_num1.get())
    num2 = int(get_num2.get())

    multy = num1 * num2
    resultbox.delete(0, "end")
    resultbox.insert(0, multy)

def divide():
    num1 = int(get_num1.get())
    num2 = int(get_num2.get())

    divide = num1 / num2
    resultbox.delete(0, "end")
    resultbox.insert(0, divide)
    print(bt4['text'])



root = Tk()
root.title("Calculator Program")
root.geometry("300x110")
#root.config(bg="black")

#==================== Frames ===================

######## Labels ###############

entry_num1 = Label(root, text="Number 1  : ")
entry_num1.grid(row=0, column=0)
get_num1 = Entry(root, width = 20)
get_num1.grid(row=0, column=1, columnspan = 4)

entry_num2 = Label(root, text="Number 2  : ")
entry_num2.grid(row=1, column=0)
get_num2 = Entry(root, width = 20)
get_num2.grid(row=1, column=1, columnspan = 4)


########## Buttons ###########
Label(root, text="Calculate   : ").grid(row=2, column=0)
bt1 = Button(root, text = "+", command = sum)
bt1.grid(row=2, column=1)

bt2 = Button(root,  text = "-", command = minus)
bt2.grid(row=2, column=2)

bt3 = Button(root, text = "x", command = multy)
bt3.grid(row=2, column=3)

bt4 = Button(root, text = "/", command = divide)
bt4.grid(row=2, column=4)

############# Result #################
resultbox_label = Label(root, text="Result        : ").grid(row=4, column=0)
resultbox = Entry(root,  width = 20)
resultbox.grid(row=4, column=1, columnspan = 4)

root.mainloop()
