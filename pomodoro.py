import time
from tkinter import *
from tkinter import messagebox
from playsound import playsound

root = Tk()
root.geometry("300x300")

root.title("Pomodoro by Dyaps")


minute = StringVar()
second = StringVar()

Entry (root, width = 5, font = ("Tahoma", 18, ""),textvariable=minute).place (x = 70, y = 50)
minute.set("00")

Entry (root, width = 5, font = ("Tahoma", 18, ""),textvariable=second).place (x = 180, y = 50)
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
            playsound('/home/dyaps/Documents/Programming/Python/goat.mp3')
        temp -= 1
           
pomodoroBtn = Button (root, text = "Pomodoro", bd = "3",
                      command = pomodoro).place(x = 40, y  = 120)

breakTimeBtn = Button (root, text = "Break   ", bd = "3",
                       command = shortBreak).place (x = 150, y = 120)

startBtn = Button (root, text = "Start Pomodoro", bd = "3",
                       command = startTime).place (x = 120, y = 200)

root.mainloop()