from tkinter import *
from sys import exit
import random

gui = Tk()
gui.title("Rock,paper,scissors 0.1")

topframe = Frame(gui)
topframe.pack(side=TOP)
middleframe = Frame(gui)
middleframe.pack()
global lowerframe
lowerframe = Frame(gui)
lowerframe.pack(side=BOTTOM)


#### gamling
global bank
global livebet
global backwin
livebet = 0
backwin = 0

onbook = 0

global moneywin
global moneyloss
moneywin = 0
moneyloss = 0
netchange_verdi = moneywin-moneyloss


def win():
    backwin = livebet*2
    bank += backwin

def loss():
    backwin = livebet*(-1)
    bank += backwin

bank = (onbook + netchange_verdi)
#### gamling


sm = 0
bw = 0
yw = 0

#feedcounter
global feedcounter
feedcounter = 0


if feedcounter == 20:
    lowerframe.forget()
    feedcounter = 0
    lowerframe = Frame(gui)
    lowerframe.pack(side=BOTTOM)


# note to myself; se hvis jeg kan gjør den bedere

#pickrate storage
uspa = 0
usro = 0
ussi = 0
boro = 0
bopa = 0
bosi = 0

#spampreventer
spampreventer = 0

if spampreventer == 0:
    botrange1 = 1
    botrange2 = 3

if spampreventer==1: # = 1 slås den på
    if usro == 0 and uspa == 0:
        botrange1 = 1
        botrange2 = 1
    if ussi == 0 and uspa == 0:
        botrange1 = 2
        botrange2 = 2
    if usro == 0 and ussi == 0:
        botrange1 = 3
        botrange2 = 3



def stop():
    gui.destroy()
    exit()

## aktiverer feedclear
def feedclear():
    global lowerframe
    global feedcounter
    lowerframe.forget()
    feedcounter = 0
    lowerframe = Frame(gui)
    lowerframe.pack(side=BOTTOM)

def showstat():
    stat = Tk()
    stat.title("statestic")
    def statstop():
        stat.destroy()
        exit()
    statframe = Frame(stat)
    statframe.pack(side=TOP)
    picks = Frame(stat)
    picks.pack(side=BOTTOM)
    sdb = Button(statframe, text="close window", fg="blue", command=statstop)
    sdb.pack(side=LEFT)
    youstat = Frame(stat)
    youstat.pack(side=TOP)
    botstat = Frame(stat)
    botstat.pack(side=TOP)
    mywins = "Wins; " + str(yw)
    myloss = "Losses; " + str(bw)
    mystale = "Stalemates; " + str(sm)
    height = 4
    width = 2
    for i in range(height):
        for j in range(width):
            bl1 = Label(picks, text="-")
            bl1.grid(row=1, column=1)
            b = Label(picks, text="rock")
            b.grid(row=1, column=2)
            b = Label(picks, text="paper")
            b.grid(row=1, column=3)
            b = Label(picks, text="scissor")
            b.grid(row=1, column=4)
            b = Label(picks, text="You")
            b.grid(row=2, column=1)
            b = Label(picks, text= usro)
            b.grid(row=2, column=2)
            b = Label(picks, text= uspa)
            b.grid(row=2, column=3)
            b = Label(picks, text=ussi)
            b.grid(row=2, column=4)
            b = Label(picks, text="Bot")
            b.grid(row=3, column=1)
            b = Label(picks, text=boro)
            b.grid(row=3, column=2)
            b = Label(picks, text=bopa)
            b.grid(row=3, column=3)
            b = Label(picks, text=bosi)
            b.grid(row=3, column=4)
    totalbattels = (sm + bw + yw)
    lossrate = (bw / totalbattels)*100
    winrate = (yw / totalbattels)*100
    mylossrate = " Lossrate | " + str(lossrate) + " %"
    mywinrate = " Winrate | " + str(winrate) + " %"
    printmystat_wins = Label(youstat, text=mywins)
    printmystat_wins.pack()
    printmystat_loss = Label(youstat, text=myloss)
    printmystat_loss.pack()
    printmystat_sm = Label(youstat, text=mystale)
    printmystat_sm.pack()
    spacer = Label(botstat, text="----------")
    spacer.pack(side=TOP)
    printmystat_wr = Label(botstat, text=mywinrate)
    printmystat_wr.pack(side=TOP)
    printmystat_lr = Label(botstat, text=mylossrate)
    printmystat_lr.pack(side=TOP)
    spacer = Label(botstat, text="----------")
    spacer.pack(side=BOTTOM)
    ecostat = Frame(stat)
    ecostat.pack(side=BOTTOM)
    spacer = Label(ecostat, text="----------")
    spacer.pack(side=BOTTOM)
    losslable = ("Total loss = " + str(moneyloss))
    winlable = ("Total winnings = " + str(moneywin))
    losslable1 = Label(ecostat, text=losslable)
    losslable1.pack(side=BOTTOM)
    losslable2 = Label(ecostat, text=winlable)
    losslable2.pack(side=BOTTOM)
    netchange_verdi = moneywin-moneyloss
    netchangelable = ("Net change = " + str(netchange_verdi))
    if netchange_verdi < 0:
        netchange_color = "RED"
    if netchange_verdi > 0:
        netchange_color = "GREEN"
    if netchange_verdi == 0:
        netchange_color = "GREEN"
    lable_netchange = Label(ecostat, text=netchangelable, fg=netchange_color)
    lable_netchange.pack(side=BOTTOM)

def rock():
    global bank
    global livebet
    global moneywin
    global moneyloss
    global backwin
    bot = random.randint(botrange1, botrange2)
    global feedcounter
    feedcounter += 1
    global usro
    global uspa
    global ussi
    global boro
    global bopa
    global bosi
    user = 1
    usro += 1
    global bw
    global yw
    global sm
    if user == bot:
        printfuver = ("Stalemate, booth players choose rocks")
        printfu = Label(lowerframe, text=printfuver, fg="blue")
        printfu.pack(side=BOTTOM)
        sm += 1
        boro +=1
    if user == 1 and bot == 2:
        printfuver = ("Paper covers rock, bot wins! ")
        printfu = Label(lowerframe, text=printfuver, fg="red")
        printfu.pack(side=BOTTOM)
        bw += 1
        bopa +=1
        backwin = livebet * (-1)
        moneyloss += livebet

    if user == 1 and bot == 3:
        printfuver = ("Rock crushes scissors, you win! ")
        printfu = Label(lowerframe, text=printfuver, fg="green")
        printfu.pack(side=BOTTOM)
        yw += 1
        bosi += 1
        backwin = livebet*2
        moneywin += livebet

def paper():
    global bank
    global livebet
    global backwin
    global moneywin
    global moneyloss
    bot = random.randint(botrange1, botrange2)
    global feedcounter
    feedcounter += 1
    global usro
    global uspa
    global ussi
    global boro
    global bopa
    global bosi
    user = 2
    uspa += 1
    global bw
    global sm
    global yw
    if user == bot:
        printfuver = ("Stalemate, booth players choose paper")
        printfu = Label(lowerframe, text=printfuver, fg="blue")
        printfu.pack(side=BOTTOM)
        sm += 1
        bopa +=1
    if user == 2 and bot == 1:
        printfuver = ("Paper covers rock, you win! ")
        printfu = Label(lowerframe, text=printfuver, fg="green")
        printfu.pack(side=BOTTOM)
        yw += 1
        boro +=1
        backwin = livebet*2
        moneywin += livebet

    if user == 2 and bot == 3:
        printfuver = ("Scissors cut paper, bot win! ")
        printfu = Label(lowerframe, text=printfuver, fg="red")
        printfu.pack(side=BOTTOM)
        bw += 1
        bosi += 1
        backwin = livebet * (-1)
        moneyloss += livebet

def scissors():
    global bank
    global moneywin
    global moneyloss
    global livebet
    global backwin
    bot = random.randint(botrange1, botrange2)
    global feedcounter
    feedcounter += 1
    global usro
    global uspa
    global ussi
    global boro
    global bopa
    global bosi
    user = 3
    ussi += 1
    global bw
    global yw
    global sm
    if user == bot:
        printfuver = ("Stalemate, booth players choose scissors")
        printfu = Label(lowerframe, text=printfuver, fg="blue")
        printfu.pack(side=BOTTOM)
        sm += 1
        bosi += 1
    if user == 3 and bot == 1:
        printfuver = ("Rock crushes scissors, bot win! ")
        printfu = Label(lowerframe, text=printfuver, fg="red")
        printfu.pack(side=BOTTOM)
        bw += 1
        boro +=1
        backwin = livebet * (-1)
        moneyloss += livebet
    if user == 3 and bot == 2:
        printfuver = ("Scissors cut paper, you win! ")
        printfu = Label(lowerframe, text=printfuver, fg="green")
        printfu.pack(side=BOTTOM)
        yw += 1
        bopa +=1
        backwin = livebet*2
        moneywin += livebet


##topframe
button1 = Button(topframe, text="exit", fg="blue", command=stop)
button1.pack(side=LEFT)

clearbutton = Button(topframe, text= "clear feed", fg="blue", command=feedclear)
clearbutton.pack(side=RIGHT)

button2 = Button(topframe, text="show stats", fg="blue", command=showstat)
button2.pack(side=RIGHT)

intro = Label(topframe, text= "Rock–paper–scissors",font=("Courier", 14),fg="blue")
intro.pack()



##middleframe
buttonr = Button(topframe, text="rock", fg="blue", command=rock)
buttonr.pack(side=LEFT)


buttons = Button(topframe, text="paper", fg="blue", command=paper)
buttons.pack(side=LEFT)


buttonp = Button(topframe, text="scissors", fg="blue", command=scissors)
buttonp.pack(side=LEFT)
