from cProfile import label
from glob import glob
from operator import index
from tkinter import *
from PIL import ImageTk, Image
import glob

root = Tk()
root.title('Image viewer')
root.iconbitmap('')

#my_img1 = ImageTk.PhotoImage(Image.open('F:/blog2/New folder (2)/#20220204_072206.jpg'))
#my_img2 = ImageTk.PhotoImage(Image.open('F:/blog2/New folder (2)/#20220210_145414.jpg'))
#my_img3 = ImageTk.PhotoImage(Image.open('F:/blog2/New folder (2)/#20220215_103329.jpg'))
#my_img4 = ImageTk.PhotoImage(Image.open('F:/blog2/New folder (2)/#20220204_073751.jpg'))
#my_img5 = ImageTk.PhotoImage(Image.open('F:/blog2/New folder (2)/#20220206_123324.jpg'))
#
#image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

image_list = []
for filename in glob.glob('F:/blog2/New folder (2)/*.jpg'):
    im = ImageTk.PhotoImage(Image.open(filename))
    image_list.append(im)

my_label = Label(image=image_list[0])
my_label.grid(row=0, column=0, columnspan=3)

status = Label(root, text = 'Image 1 of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)


def forward(image_num):
    global my_label
    global next_button
    global back_button

    my_label.grid_forget()
    my_label = Label(image=image_list[image_num])
    next_button = Button(root, text='Next',padx=50, command=lambda: forward(image_num + 1))
    back_button = Button(root, text='Back',padx=50, command=lambda: back(image_num -1))

    if image_num == len(image_list)-1:
        next_button = Button(root, text='Next', padx=50, state=DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)

    back_button.grid(row=1, column=0)
    next_button.grid(row=1, column=2)

    status = Label(root, text = 'Image '+ str(image_num + 1)  +' of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(image_num):
    global my_label
    global next_button
    global back_button

    my_label.grid_forget()
    my_label = Label(image=image_list[image_num])
    next_button = Button(root, text='Next',padx=50, command=lambda:forward(image_num + 1))
    back_button = Button(root, text='Back',padx=50, command=lambda: back(image_num -1))

    if image_num == 0:
        back_button = Button(root, text='Back', padx=50, state=DISABLED)


    my_label.grid(row=0, column=0, columnspan=3)

    back_button.grid(row=1, column=0)
    next_button.grid(row=1, column=2)

    status = Label(root, text = 'Image '+ str(image_num + 1) +' of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)



exit_button = Button(root, text='Exit',padx=50, command=exit)
exit_button.grid(row=1, column=1)

next_button = Button(root, text='Next',padx=50, command=lambda: forward(1))
next_button.grid(row=1, column=2, pady= 10)

back_button = Button(root, text='Back',padx=50, command=back, state=DISABLED)
back_button.grid(row=1, column=0)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()