import time
from tkinter import *
from tkinter import messagebox
from playsound import playsound

root = Tk()
root.geometry("300x300")

root.title("Pomodoro by Dyaps")
#bg = PhotoImage (file = "BLACK.png")
#label1 = Label( root, image = bg)
#label1.place(x = 0, y = 0)

root.configure(bg = "#DFE2FE")

minute = StringVar()
second = StringVar()

Entry (root, width = 5, font = ("Tahoma", 18, ""),textvariable=minute, justify=CENTER, bg = "#B1CBFA",).place (x = 70, y = 50)
minute.set("00")

Entry (root, width = 5, font = ("Tahoma", 18, ""),textvariable=second, justify=CENTER, bg = "#B1CBFA").place (x = 180, y = 50)
second.set("00")

def pomodoro():
    minute.set("25")
    second.set("00")
    
def shortBreak():
    minute.set("05")
    second.set("00")

def startTime():
    try:
        temp = int (minute.get()) * 60 + int (second.get())
    
    except:
        print("Please input the right value")
    
    while temp >-1:
        mins,secs = divmod(temp,60)
         
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        
        root.update()
        time.sleep(1)
        
        if temp == 0:
            playsound('goat.mp3')
        temp -= 1

start = PhotoImage (file = "START1.png")

pomodoroBtn = Button (root, text = "Pomodoro", bd = "3",
                      command = pomodoro, bg="#B1CBFA").place(x = 20, y  = 218)

breakTimeBtn = Button (root, text = "Break   ", bd = "3",
                       command = shortBreak, bg="#B1CBFA").place (x = 20, y = 250)

startBtn = Button (root, text = "", image = start , compound= TOP
                       , command = startTime, bg="#B1CBFA").place (x = 100, y = 100)

root.mainloop()