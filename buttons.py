from tkinter import *
import tkinter as tk

root = Tk()	

# Open window having dimension 100x100
root.geometry('400x250')

# add bg
bg = PhotoImage(file = "bg.png")
canvas1 = Canvas(root, width=400, height=250)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image(0, 0, image = bg, anchor = "nw")

# add icons
icon1 = PhotoImage(file = "notepad_image.png", height=30, width=30)
canvas1.create_image(130, 93, image = icon1, anchor = "nw")

icon2 = PhotoImage(file = "list_image.png", height=30, width=30)
canvas1.create_image(130, 143, image = icon2, anchor = "nw")

icon3 = PhotoImage(file = "alarm_image.png", height=30, width=30)
canvas1.create_image(130, 193, image = icon3, anchor = "nw")

# add heading
canvas1.create_text(60,10, text = """                Python Mini Project
Welcome to Multi-Functional Notepad. 
           Please choose your option.""", anchor = "nw", fill = "black", font = ("Cooper Black", 11))

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
btn = Button(root, text = 'Notepad', bd = '7', bg = "#f27e90", command = notepad)
btn.place(x=170,y=90)

btn2 = Button(root, text = 'To-Do List', bd = '7', bg = "#f27e90", command = todo )
btn2.place(x=170,y=140)

btn3 = Button(root, text = 'Alarm', bd = '7', bg = "#f27e90", command = alarm )
btn3.place(x=170,y=190)

root.mainloop()
