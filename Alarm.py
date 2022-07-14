from tkinter import *
import datetime
import time
from playsound import playsound
from tkinter import messagebox
 
def Alarm(set_alarm_timer,reminder):
    while True:
        time.sleep(1)
        actual_time = datetime.datetime.now()
        cur_time = actual_time.strftime("%H:%M:%S")
        msg="Current Time: "+str(cur_time)
        print(msg) 
        if cur_time == set_alarm_timer:
            print("REMINDER ALERT!!!",reminder)
            playsound("Clock-sound-effect.mp3")            
            break

def get_alarm_time():
    alarm_set_time = f"{hour.get()}:{min.get()}:{sec.get()}"
    reminder1 = f"{reminder.get()}"
    Alarm(alarm_set_time,reminder1)

def exitapp():
    confex = messagebox.askquestion(
        'Quit confirmation', 'Are you sure you want to quit?')
    if confex.upper() == "YES":
        window.destroy()
    else:
        pass
def mainmenu():
    window.destroy()
    import main
 
window = Tk()
window.title("Alarm Clock")
window.geometry("400x300")
window.config(bg="#062C30")
window.resizable(width=False,height=False)
window.wm_iconbitmap("alarm_icon.ico")

time_format=Label(window, text= "Remember to set time in 24 hour format!!!", fg="#F5F5F5", bg="#062C30",font=("Arial",13)).place(x=50,y=140)
addTime = Label(window,text = "Hour    Min    Sec",font=60, fg="#F5F5F5",bg="#062C30").place(x = 210, y = 15)
setYourAlarm = Label(window,text = "Set Time for Alarm: ",fg="#E2D784",bg="#062C30",font=("Helevetica",15,"bold")).place(x=10, y=40)
setYourAlarm = Label(window,text = "Enter Reminder: ",fg="#E2D784",bg="#062C30", font=("Helevetica",15,"bold")).place(x=10, y=100)
 
hour = StringVar()
min = StringVar()
sec = StringVar()
reminder = StringVar()
 
hourTime= Entry(window,textvariable = hour, fg = "#E2D784", bg = "#05595B",width = 4,font=(20)).place(x=210,y=45)
minTime= Entry(window,textvariable = min, fg = "#E2D784", bg = "#05595B",width = 4,font=(20)).place(x=270,y=45)
secTime = Entry(window,textvariable = sec, fg = "#E2D784", bg = "#05595B",width = 4,font=(20)).place(x=330,y=45)
rem_inder = Entry(window, textvariable=reminder, fg = "#F5F5F5", bg = "#05595B",width = 15,font=(20)).place(x=200,y=100)

submit = Button(window,text = "Set Your Alarm",fg="Black",bg="#E2D784",width = 15,bd=0,command = get_alarm_time,font=(13)).place(x =120,y=180)
submit = Button(window,text = "Exit Alarm",fg="Black",bg="#E2D784",width = 10,bd=0,command = exitapp,font=(13)).place(x =85,y=221)
submit = Button(window,text = "Main Menu",fg="Black",bg="#E2D784",width = 10,bd = 0,command = mainmenu,font=(13)).place(x=205,y=221)
 
window.mainloop()
