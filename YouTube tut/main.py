from fileinput import filename
from genericpath import isfile
import imp
import tkinter as tk
from tkinter import Label, filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename= filedialog.askopenfilename(initialdir="/", title= "select file", filetypes=(("executables","*.exe"),("all files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()
def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=500, width=500, bg="#000000")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="open file", padx=10, pady= 5, fg="white", bg="black", command=addApp)
openFile.pack()

openApp = tk.Button(root, text="open app", padx=10, pady= 5, 
fg="white", bg="black", command=runApps)
openApp.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')