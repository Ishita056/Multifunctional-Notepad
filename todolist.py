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


root.mainloop()