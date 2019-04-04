from tkinter import *
from tkinter import message
root = Tk()

label = Label(root, text="welcome, please input your name")
label.pack()

entry = Entry(root)
entry.pack()

button = Button(root, text="enter")
button.pack()

root.pack()
