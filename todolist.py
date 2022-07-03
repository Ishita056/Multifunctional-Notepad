from tkinter import *
import random
from tkinter import messagebox

# defining functions
def updatetask():
    clearlistbox()
    for utask in tasks:
        lbltask.insert("end", utask)
    numtask = len(tasks)
    lbldsp_count['text'] = numtask


def clearlistbox():
    lbltask.delete(0, "end")


def addtask():
    lbldisplay["text"] = ""
    Ntask = txtinput.get()
    if Ntask != "":
        tasks.append(Ntask)
        updatetask()
    else:
        lbldisplay["text"] = "please enter the text"
    txtinput.delete(0, 'end')


def deleteone():
    delt = lbltask.get("active")
    if delt in tasks:
        tasks.remove(delt)
    updatetask()


# making window
root = Tk()
root.configure(bg="white")
root.title("To-Do List")
root.geometry("300x400")
tasks = []

lbltitle = Label(root, text="Todo List", bg="white")
lbltitle.grid(row=0, column=0)

lbldisplay = Label(root, text="", bg="white")
lbldisplay.grid(row=0, column=1)

lbldsp_count = Label(root, text="", bg="white")
lbldsp_count.grid(row=0, column=3)

txtinput =Entry(root, width=15)
txtinput.grid(row=1, column=1)

# adding buttons
txtadd_button = Button(
    root, text="Add todo", bg="white", fg="red", width=15, command=addtask)
txtadd_button.grid(row=1, column=0)

delonebutton = Button(
    root, text="Done Task", bg="white", width=15, command=deleteone)
delonebutton.grid(row=2, column=0)


# display tasks
lbltask = Listbox(root)
lbltask.grid(row=2, column=1, rowspan=7, columnspan=4)



root.mainloop() 
