from tkinter import *
import random
from tkinter import messagebox

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

def deleteall():
    conf = messagebox.askquestion('Delete all??', 'are you sure to delete all task?')
    # print(conf)
    if conf.upper() == "YES":
        global tasks
        tasks = []
        updatetask()
    else:
        pass

def deleteone():
    delt = lbltask.get("active")
    if delt in tasks:
        tasks.remove(delt)
    updatetask()

def sortasc():
    tasks.sort()
    updatetask()

def sortdsc():
    tasks.sort(reverse=True)
    updatetask()

def randomtsk():
    randtask = random.choice(tasks)
    lbldisplay["text"] = randtask

def saveact():
    savecon = messagebox.askquestion('Save confirmation', 'Save Your Progress?')
    if savecon.upper() == "YES":
        with open("SaveFile.txt", "w") as filehandle:
            for listitem in tasks:
                filehandle.write('%s\n' % listitem)
    else:
        pass

def exitapp():
    confex = messagebox.askquestion(
        'Quit confirmation', 'Are you sue you want to quit?')
    if confex.upper() == "YES":
        root.destroy()
    else:
        pass

root = Tk()
root.configure(bg="white")
root.title("To-Do List")
root.geometry("255x250")
root.wm_iconbitmap("list_icon.ico")
tasks = []

#title
lbltitle = Label(root, text="Todo List", bg="white")
lbltitle.grid(row=0, column=0)

#display window
lbldisplay = Label(root, text="", bg="white")
lbldisplay.grid(row=0, column=1)

# counting tasks
lbldsp_count = Label(root, text="", bg="white")
lbldsp_count.grid(row=0, column=3)

# enter text
txtinput =Entry(root, width=15)
txtinput.grid(row=1, column=1)

# adding buttons
txtadd_button = Button(root, text="Add todo", bg="white", fg="red", width=15, command=addtask)
txtadd_button.grid(row=1, column=0)

delonebutton = Button(root, text="Done Task", bg="white", width=15, command=deleteone)
delonebutton.grid(row=2, column=0)

delallbutton = Button(root, text="Delete all", bg="white", width=15, command=deleteall)
delallbutton.grid(row=3, column=0)

sortasc = Button(root, text="sort (ASC)", bg="White", width=15, command=sortasc)
sortasc.grid(row=4, column=0)

sortdsc = Button(root, text="sort (DSC)", bg="White", width=15, command=sortdsc)
sortdsc.grid(row=5, column=0)

randombutton = Button(root, text="random task", bg="White", width=15, command=randomtsk)
randombutton.grid(row=6, column=0)

savebutton = Button(root, text="save TodoList", bg="white", width=15, command=saveact)
savebutton.grid(row=7, column=0)

exitbutton = Button(root, text="exit app", bg="white", width=15, command=exitapp)
exitbutton.grid(row=8, column=0)

# display tasks
lbltask = Listbox(root)
lbltask.grid(row=2, column=1, rowspan=12, columnspan=2)

# main loop
root.mainloop()
