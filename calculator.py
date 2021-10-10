from tkinter import *
from decimal import Decimal

FONT = "Calibri 19"
WIDTH = 5
HEIGHT = 2

root = Tk()
root.title("Calculator")


def num_click(number):
    current = entry.get()
    if current == "0":
        current = ""
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def clear_click():
    entry.delete(0, END)
    entry.insert(0, "0")


def float_click():
    current = entry.get()
    if "." in current:
        pass
    else:
        entry.delete(0, END)
        entry.insert(0, str(current) + ".")


def add_click():
    global first_num
    global operator
    first_num = entry.get()
    operator = "add"
    entry.delete(0, END)


def sub_click():
    global first_num
    global operator
    first_num = entry.get()
    operator = "sub"
    entry.delete(0, END)


def mul_click():
    global first_num
    global operator
    first_num = entry.get()
    operator = "mul"
    entry.delete(0, END)


def div_click():
    global first_num
    global operator
    first_num = entry.get()
    operator = "div"
    entry.delete(0, END)


def equal_click():
    global first_num
    second_num = entry.get()
    second_num = Decimal(second_num)
    try:
        first_num = Decimal(first_num)
    except:
        first_num = 0
    entry.delete(0, END)

    if operator == "add":
        result = first_num + second_num
        result = float(result)
        if result.is_integer():
            result = int(result)
        entry.insert(0, result)

    if operator == "sub":
        result = first_num - second_num
        result = float(result)
        if result.is_integer():
            result = int(result)
        entry.insert(0, result)
    
    if operator == "mul":
        result = first_num * second_num
        result = float(result)
        if result.is_integer():
            result = int(result)
        entry.insert(0, result)

    if operator == "div":
        try:
            result = first_num / second_num
            result = float(result)
            if result.is_integer():
                result = int(result)
            entry.insert(0, result)  
        except ZeroDivisionError:
            entry.insert(0, "ERROR")
    

entry = Entry(root, width=10, borderwidth=5, font="Calibri 25")
entry.grid(row=0, column=0, columnspan=3)
entry.insert(0, "0")

button_7 = Button(root, text="7", width=WIDTH, height=HEIGHT, font=FONT, command=lambda: num_click(7))
button_8 = Button(root, text="8", width=WIDTH, height=HEIGHT, font=FONT, command=lambda: num_click(8))
button_9 = Button(root, text="9", width=WIDTH, height=HEIGHT, font=FONT, command=lambda: num_click(9))
button_4 = Button(root, text="4", width=WIDTH, height=HEIGHT, font=FONT, command=lambda: num_click(4))
button_5 = Button(root, text="5", width=WIDTH, height=HEIGHT, font=FONT, command=lambda: num_click(5))
button_6 = Button(root, text="6", width=WIDTH, height=HEIGHT, font=FONT, command=lambda: num_click(6))
button_1 = Button(root, text="1", width=WIDTH, height=HEIGHT, font=FONT, command=lambda: num_click(1))
button_2 = Button(root, text="2", width=WIDTH, height=HEIGHT, font=FONT, command=lambda: num_click(2))
button_3 = Button(root, text="3", width=WIDTH, height=HEIGHT, font=FONT, command=lambda: num_click(3))
button_0 = Button(root, text="0", width=WIDTH, height=HEIGHT, font=FONT, command=lambda: num_click(0))

button_float = Button(root, text=".", width=WIDTH, height=HEIGHT, font=FONT, command=float_click)
button_equal = Button(root, text="=", width=WIDTH, height=HEIGHT, font=FONT, command=equal_click)

button_clear = Button(root, text="Clear", width=WIDTH, height=HEIGHT, font=FONT, command=clear_click)
button_div = Button(root, text="/", width=WIDTH, height=HEIGHT, font=FONT, command=div_click)
button_mul = Button(root, text="*", width=WIDTH, height=HEIGHT, font=FONT, command=mul_click)
button_sub = Button(root, text="-", width=WIDTH, height=HEIGHT, font=FONT, command=sub_click)
button_add = Button(root, text="+", width=WIDTH, height=HEIGHT, font=FONT, command=add_click)


button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1 , column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2 , column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3 , column=2)

button_0.grid(row=4, column=0)
button_float.grid(row=4, column=1)
button_equal.grid(row=4, column=2)

button_clear.grid(row=0, column=4)
button_div.grid(row=1, column=4)
button_mul.grid(row=2, column=4)
button_sub.grid(row=3, column=4)
button_add.grid(row=4, column=4)

root.mainloop()