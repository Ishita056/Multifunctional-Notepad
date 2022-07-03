from tkinter import *
import random
from tkinter import messagebox


root = Tk()
root.configure(bg="white")
root.title("To-Do List")
root.geometry("300x400")
tasks = []

lbltitle = Label(root, text="Todo List", bg="white")
lbltitle.grid(row=0, column=0)

lbldisplay = Label(root, text="", bg="white")
lbldisplay.grid(row=0, column=1, columnspan=4)

lbldsp_count = Label(root, text="", bg="white")
lbldsp_count.grid(row=0, column=3)

txtinput =Entry(root, width=15)
txtinput.grid(row=1, column=1)

root.mainloop() 
