from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()


def myClick():
    myLabel = Label(root, text= 'hello ' + e.get())
    myLabel.pack()

myButton = Button(root, text='click', padx=50, pady=10, command=myClick)
myButton.pack()

root.mainloop()