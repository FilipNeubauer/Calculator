from tkinter import *

FONT = "Calibri 19"
WIDTH = 5
HEIGHT = 2

root = Tk()
root.title("Calculator")

entry = Entry(root, width=10, borderwidth=5, font="Calibri 25")
entry.grid(row=0, column=0, columnspan=3)


button_7 = Button(root, text="7", width=WIDTH, height=HEIGHT, font=FONT)
button_8 = Button(root, text="8", width=WIDTH, height=HEIGHT, font=FONT)
button_9 = Button(root, text="9", width=WIDTH, height=HEIGHT, font=FONT)
button_4 = Button(root, text="4", width=WIDTH, height=HEIGHT, font=FONT)
button_5 = Button(root, text="5", width=WIDTH, height=HEIGHT, font=FONT)
button_6 = Button(root, text="6", width=WIDTH, height=HEIGHT, font=FONT)
button_1 = Button(root, text="1", width=WIDTH, height=HEIGHT, font=FONT)
button_2 = Button(root, text="2", width=WIDTH, height=HEIGHT, font=FONT)
button_3 = Button(root, text="3", width=WIDTH, height=HEIGHT, font=FONT)
button_0 = Button(root, text="0", width=WIDTH, height=HEIGHT, font=FONT)

button_float = Button(root, text=".", width=WIDTH, height=HEIGHT, font=FONT)
button_equal = Button(root, text="=", width=WIDTH, height=HEIGHT, font=FONT)

button_clear = Button(root, text="Clear", width=WIDTH, height=HEIGHT, font=FONT)
button_div = Button(root, text="/", width=WIDTH, height=HEIGHT, font=FONT)
button_mul = Button(root, text="*", width=WIDTH, height=HEIGHT, font=FONT)
button_sub = Button(root, text="-", width=WIDTH, height=HEIGHT, font=FONT)
button_add = Button(root, text="+", width=WIDTH, height=HEIGHT, font=FONT)


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