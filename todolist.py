from tkinter import *
import random
from tkinter import messagebox
from tkinter import font

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
        lbldisplay["text"] = "Please enter the text"
    txtinput.delete(0, 'end')

def deleteall():
    conf = messagebox.askquestion('Delete all??', 'Are you sure to delete all task?')
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
    numtask=len(tasks)
    if numtask == 0:
        lbldisplay["text"] = "Please enter the text"
    else:
        randtask = random.choice(tasks)
        lbldisplay["text"] = randtask

def saveact():
    savecon = messagebox.askquestion('Save Confirmation', 'Save Your Progress?')
    if savecon.upper() == "YES":
        with open("SaveFile.txt", "w") as filehandle:
            for listitem in tasks:
                filehandle.write('%s\n' % listitem)
    else:
        pass

def exitapp():
    confex = messagebox.askquestion(
        'Quit Confirmation', 'Are you sue you want to quit?')
    if confex.upper() == "YES":
        root.destroy()
    else:
        pass

def mainmenu():
    root.destroy()
    import main

# making tk window
root = Tk()
root.configure(bg="#121212")
root.title("To-Do List")
root.geometry("325x270")
root.resizable(width=False,height=False)
root.wm_iconbitmap("list_icon.ico")
root.config(bg="#121212")
tasks = []

#title
lbltitle = Label(root, text="Choose Option", fg = "white", bg="#121212", font = ("Cambria",10))
lbltitle.place(x = 5, y = 0)

#display window
lbldisplay = Label(root, text="", font = ("Cambria",10), bg="#121212", fg = "white")
lbldisplay.place(x = 120, y = 0)

# counting tasks
lbldsp_count = Label(root, text="", font = ("Cambria",11), bg="#121212", fg = "white")
lbldsp_count.place(x = 305, y = 0)

# enter text
txtinput =Entry(root, width=15, bd = 0, bg = "#F5F5F5")
txtinput.place(x = 120, y = 21, width = 200, height = 25)

# adding buttons
txtadd_button = Button(root, text="Add todo", bg="#F05454", fg="#121212", bd = 0, font = ("Calibri",10,font.BOLD), width=14, command=addtask)
txtadd_button.place(x = 5,y = 21, height = 26)

delonebutton = Button(root, text="Done Task", bg="#30475E", fg = "#F5F5F5", bd = 0, font = ("Calibri",10), width=14, command=deleteone)
delonebutton.place(x = 5,y = 50, height = 25)

delallbutton = Button(root, text="Delete all", bg="#30475E", fg = "#F5F5F5", bd = 0, font = ("Calibri",10), width=14, command=deleteall)
delallbutton.place(x = 5,y = 76, height = 25)

sortasc = Button(root, text="Sort (ASC)", bg="#30475E", fg = "#F5F5F5", bd = 0, font = ("Calibri",10), width=14, command=sortasc)
sortasc.place(x = 5,y = 102, height = 25)

sortdsc = Button(root, text="Sort (DSC)", bg="#30475E", fg = "#F5F5F5", bd = 0, font = ("Calibri",10), width=14, command=sortdsc)
sortdsc.place(x = 5,y = 128, height = 25)

randomtsk = Button(root, text="Random task", bg="#30475E", fg = "#F5F5F5", bd = 0, font = ("Calibri",10), width=14, command=randomtsk)
randomtsk.place(x = 5,y = 154, height = 25)

savebutton = Button(root, text="Save TodoList", bg="#30475E", fg = "#F5F5F5", bd = 0, font = ("Calibri",10), width=14, command=saveact)
savebutton.place(x = 5,y = 180, height = 25)

exitbutton = Button(root, text="Exit app", bg="#30475E", fg = "#F5F5F5", bd = 0, font = ("Calibri",10), width=14, command=exitapp)
exitbutton.place(x = 5,y = 206, height = 25)

mainmenu = Button(root, text = "Back to MainMenu", bg = "#F05454", fg="#121212", bd = 0, font = ("Calibri",10,font.BOLD), width = 25, command = mainmenu)
mainmenu.place(x = 70, y = 235, height = 26)

# display tasks
lbltask = Listbox(root, bd = 0, bg = "#F5F5F5")
lbltask.place(x = 120, y = 50, width=200, height=180)

# main loop
root.mainloop()
