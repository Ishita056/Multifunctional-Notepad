def Alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        actual_time = datetime.datetime.now()
        cur_time = actual_time.strftime("%H:%M:%S") 
        cur_date = actual_time.strftime("%d/%m/%Y")
        msg="Current Time: "+str(cur_time)
        
        print(msg) 
        if cur_time == set_alarm_timer:
            playsound("Clock-sound-effect.mp3")
            break

def get_alarm_time():
    alarm_set_time = f"{hour.get()}:{min.get()}:{sec.get()}"
    Alarm(alarm_set_time)

def exitapp():
    confex = messagebox.askquestion(
        'Quit confirmation', 'Are you sure you want to quit?')
    if confex.upper() == "YES":
        window.destroy()
    else:
        pass
