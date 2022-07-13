from tkinter import *
import tkinter as tk
from tkinter.font import BOLD

root = Tk()	
root.title("Main Menu")

# Open window having dimension 100x100
root.geometry('800x500')
root.resizable(width=False,height=False)

# add bg
bg = PhotoImage(file = "bg.png")
canvas1 = Canvas(root, width=400, height=250, bg = "#fbecab")
canvas1.pack(fill = "both", expand = True)
canvas1.create_image(0, 0, image = bg, anchor = "nw")

# add icons
icon1 = PhotoImage(file = "notepad_image.png", height=40, width=40)
canvas1.create_image(300, 216, image = icon1, anchor = "nw")

icon2 = PhotoImage(file = "list_image.png", height=40, width=40)
canvas1.create_image(300, 289, image = icon2, anchor = "nw")

icon3 = PhotoImage(file = "alarm_image.png", height=40, width=40)
canvas1.create_image(300, 359, image = icon3, anchor = "nw")

# add heading
canvas1.create_text(160,40, text = """                   Python Mini Project
Welcome to Multi-Functional Notepad. 
              Please choose your option.""", anchor = "nw", fill = "#000000", font = ("Cambria", 22, BOLD))

def notepad():
    root.destroy()
    import notepad_file

def todo():
    root.destroy()
    import todolist

def alarm():
    root.destroy()
    import Alarm

# Create a Button
btn = Button(root, height=1, width=12, text = 'Notepad', fg = "White", font = ("Century Gothic",12,BOLD), bd = '7', bg = "#F18712", command = notepad)
btn.place(x=350,y=210)

btn2 = Button(root, height=1, width=12, text = 'To-Do List', fg = "White", font = ("Century Gothic",12,BOLD), bd = '7', bg = "#F15412", command = todo )
btn2.place(x=350,y=280)

btn3 = Button(root, height=1, width=12, text = 'Alarm', fg = "White", font = ("Century Gothic",12,BOLD), bd = '7', bg = "#873e23", command = alarm )
btn3.place(x=350,y=350)

root.mainloop()
