from ast import Lambda
from logging import root
import math
from tkinter import *

root = Tk()
root.title('Simple Calculator')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_add(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clear():
    e.delete(0, END)

def add_sum():
    first_num = e.get()
    global f_num
    global s_math
    s_math = 'addition'
    f_num = float(first_num)
    e.delete(0, END)

def subract():
    first_num = e.get()
    global f_num
    global s_math
    s_math = 'subtraction'
    f_num = float(first_num)
    e.delete(0, END)


def divide():
    first_num = e.get()
    global f_num
    global s_math
    s_math = 'divide'
    f_num = float(first_num)
    e.delete(0, END)


def multiply():
    first_num = e.get()
    global f_num
    global s_math
    s_math = 'multiply'
    f_num = float(first_num)
    e.delete(0, END)


def equal():
    second_num = e.get()
    e.delete(0, END)
    if s_math == 'addition':
        e.insert(0, f_num + float(second_num))
    if s_math == 'subtration':
        e.insert(0, f_num - float(second_num))
    if s_math == 'divide':
        e.insert(0, f_num / float(second_num))
    if s_math == 'multiply':
        e.insert(0, f_num * float(second_num))

#cal buttons and layout
button_1 = Button(root, text= '1', padx=40,pady=20, command=lambda: button_add(1))
button_2 = Button(root, text= '2', padx=40,pady=20, command=lambda: button_add(2))
button_3 = Button(root, text= '3', padx=40,pady=20, command=lambda: button_add(3))
button_4 = Button(root, text= '4', padx=40,pady=20, command=lambda: button_add(4))
button_5 = Button(root, text= '5', padx=40,pady=20, command=lambda: button_add(5))
button_6 = Button(root, text= '6', padx=40,pady=20, command=lambda: button_add(6))
button_7 = Button(root, text= '7', padx=40,pady=20, command=lambda: button_add(7))
button_8 = Button(root, text= '8', padx=40,pady=20, command=lambda: button_add(8))
button_9 = Button(root, text= '9', padx=40,pady=20, command=lambda: button_add(9))
button_0 = Button(root, text= '0', padx=40,pady=20, command=lambda: button_add(0))

button_clear = Button(root, text= 'C', padx=39,pady=20, command=clear)
button_equal = Button(root, text= '=', padx=39,pady=82, command=equal)

button_sum = Button(root, text= '+', padx=40,pady=20, command=add_sum)
button_minus = Button(root, text= '-', padx=40,pady=20, command=subract)
button_divide = Button(root, text= '/', padx=40,pady=20, command=divide)
button_multi = Button(root, text= 'x', padx=40,pady=20, command=multiply)




button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)

button_equal.grid(row=4, column=2, rowspan=3)
button_clear.grid(row=5, column=1)

button_sum.grid(row=4, column=0)
button_minus.grid(row=5, column=0)
button_divide.grid(row=6, column=0)
button_multi.grid(row=6, column=1)

root.mainloop()