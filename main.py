from tkinter import *
from sys import exit
import random

gui = Tk()
gui.title("Rock,paper,scissors 0.1")


topframe = Frame(gui)
topframe.pack(side=TOP)
middleframe = Frame(gui)
middleframe.pack()
lowerframe = Frame(gui)
lowerframe.pack(side=BOTTOM)

sm = 0
bw = 0
yw = 0

def stop():
    gui.destroy()
    exit()

def rock():
    bot = random.randint(1,3)
    user = 1
    global bw
    global yw
    global sm
    if user == bot:
        printfuver = ("Stalemate, booth players choose rocks")
        printfu = Label(lowerframe, text=printfuver, fg="blue")
        printfu.pack()
        sm += 1
    if user == 1 and bot == 2:
        printfuver = ("Paper covers rock, bot wins! ")
        printfu = Label(lowerframe, text=printfuver, fg="red")
        printfu.pack()
        bw += 1
    if user == 1 and bot == 3:
        printfuver = ("Rock crushes scissors, you win! ")
        printfu = Label(lowerframe, text=printfuver, fg="green")
        printfu.pack()
        yw += 1

def paper():
    bot = random.randint(1,3)
    user = 2
    global bw
    global sm
    global yw
    if user == bot:
        printfuver = ("Stalemate, booth players choose paper")
        printfu = Label(lowerframe, text=printfuver, fg="blue")
        printfu.pack()
        sm += 1
    if user == 2 and bot == 1:
        printfuver = ("Paper covers rock, you win! ")
        printfu = Label(lowerframe, text=printfuver, fg="green")
        printfu.pack()
        yw += 1
    if user == 2 and bot == 3:
        printfuver = ("Scissors cut paper, bot win! ")
        printfu = Label(lowerframe, text=printfuver, fg="red")
        printfu.pack()
        bw += 1

def scissors():
    bot = random.randint(1,3)
    user = 3
    global bw
    global yw
    global sm
    if user == bot:
        printfuver = ("Stalemate, booth players choose scissors")
        printfu = Label(lowerframe, text=printfuver, fg="blue")
        printfu.pack()
        sm += 1
    if user == 3 and bot == 1:
        printfuver = ("Rock crushes scissors, bot win! ")
        printfu = Label(lowerframe, text=printfuver, fg="red")
        printfu.pack()
        bw += 1
    if user == 3 and bot == 2:
        printfuver = ("Scissors cut paper, you win! ")
        printfu = Label(lowerframe, text=printfuver, fg="green")
        printfu.pack()
        yw += 1


##topframe
button1 = Button(topframe, text="exit", fg="blue", command=stop)
button1.pack(side=LEFT)

intro = Label(topframe, text= "Rock–paper–scissors" , fg="blue")
intro.pack()


##middleframe
buttonr = Button(topframe, text="rock", fg="blue", command=rock)
buttonr.pack(side=LEFT)

buttons = Button(topframe, text="paper", fg="blue", command=paper)
buttons.pack(side=LEFT)

buttonp = Button(topframe, text="scissors", fg="blue", command=scissors)
buttonp.pack(side=LEFT)
