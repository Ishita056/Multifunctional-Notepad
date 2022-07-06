# import everything from tkinter module
from tkinter import *
import tkinter as tk

# create a tkinter window
root = Tk()	

# Create label
head = Label(root, text = """Python Mini Project
     Welcome to Multi-Functional Notepad. 
         Please choose your option.""")
head.config(font =("Courier", 14))


head.pack()

# Open window 
root.geometry('500x400')

def notepad():
    root.destroy()
    import notepad_file

def todo():
    root.destroy()
    import todolist

# Create a Button
btn1 = Button(root, text = 'Notepad', bd = '5',
						command = notepad)

# Set the position of button on the top of window.
btn1.place(x=210,y=100)
    
# Create a Button
btn2 = Button(root, text = 'To-Do List', bd = '5',
						command = todo )

# Set the position of button on the top of window.
btn2.place(x=210,y=200)

root.mainloop()
