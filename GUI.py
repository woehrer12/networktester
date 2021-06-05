from tkinter import *
import multiprocessing as mp
import tkinter
import Klassen.Ping
import time
import Klassen.Address


Address = Klassen.Address.Address_Class()
Ping = Klassen.Ping.Ping_Class()

def tick():
    Ping.check_ping("google.de")
    global utczeit
    utczeit = time.strftime('%H:%M:%S',time.gmtime())
    utcuhr.config(text = utczeit)
    utcuhr.after(200, tick) 

def createLabel():
    che = Checkbutton(window, text=address, variable=check).pack(side='left')
    lbl = Label(window, text="Not OK", background="red").pack(side='right')
    return che , lbl


ticktime = 60

window = Tk()

window.title("networktester")

utcuhr = Label(master=window,
            font=('Arial',30),
            fg='black',
            width = 10,
            height = 1)

utcuhr.pack()

lbl = Label(window, text="networktester").pack()







tick()

window.mainloop()


