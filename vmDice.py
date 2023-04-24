import random
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

root = Tk()

diceBlackAmount = 5
diceRedAmount = 5

# definere bildefiler
BlackSuccess = Image.open("WhiteSuccess.png")
BlackFailure = Image.open("WhiteFailure.png")
BlackCriticalSuccess = Image.open("WhiteCritical.png")
RedSuccess = Image.open("RedSuccess.png")
RedFailure = Image.open("RedFailure.png")
RedCriticalSuccess = Image.open("RedCritical.png")
RedCriticalFailure = Image.open("RedBestial.png")

dice = []
list.clear(dice)

def roll_dice():

    diceBlackAmount = int(black_amount_entry.get()) # Hente verdien fra input-feltet for antall svarte terninger
    diceRedAmount = int(red_amount_entry.get()) # Hente verdien fra input-feltet for antall røde terninger

    # Kode for å rulle terningene

    for i in range(diceBlackAmount):
        addDice = ["Black", random.randrange(1, 11)]
        if 10 in addDice:
            addDice.insert(3, "BLACK CRITICAL")
        elif 5 <= addDice[1] <= 9:
            addDice.insert(3, "BLACK SUCCESS")
        else:
            addDice.insert(3, "BLACK FAILURE")

        dice.append(addDice)

    for i in range(diceRedAmount):
        addDice = ["Red", random.randrange(1, 11)]
        if 1 in addDice:
            addDice.insert(3, "RED CRITICAL FAILURE")
        elif 5 <= addDice[1] <= 9:
            addDice.insert(3, "RED SUCCESS")
        elif 10 in addDice:
            addDice.insert(3, "RED CRITICAL SUCCESS")
        else:
            addDice.insert(3, "RED FAILURE")

        dice.append(addDice)

    for i in range(len(dice)):
        print(dice[i])

    for i in range(len(dice)):
        a, b, c = dice[i]
        print(a, b, c)

    diceRows = i + 1
    print(diceRows)

    # kode for å gjør klar GUI med resultater
    def update_gui():
        for i in range(len(dice)):
            a, b, c = dice[i]
            print(c)

            if "BLACK CRITICAL" in c: #2
                tkimage2= ImageTk.PhotoImage(BlackCriticalSuccess)
                diceText3 = tk.Label(frame2, image=tkimage2)
                diceText3.image = tkimage2
                diceText3.pack(anchor='c')
            elif "BLACK SUCCESS" in c: #3
                tkimage3= ImageTk.PhotoImage(BlackSuccess)
                diceText3 = tk.Label(frame2, image=tkimage3)
                diceText3.image = tkimage3
                diceText3.pack(anchor='c')
            elif "BLACK FAILURE" in c:#4
                tkimage4= ImageTk.PhotoImage(BlackFailure)
                diceText3 = tk.Label(frame2, image=tkimage4)
                diceText3.image = tkimage4
                diceText3.pack(anchor='c')
            elif "RED SUCCESS" in c:#5
                tkimage5= ImageTk.PhotoImage(RedSuccess)
                diceText3 = tk.Label(frame2, image=tkimage5)
                diceText3.image = tkimage5
                diceText3.pack(anchor='c')
            elif "RED CRITICAL FAILURE" in c: #6
                tkimage6= ImageTk.PhotoImage(RedCriticalFailure)
                diceText3 = tk.Label(frame2, image=tkimage6)
                diceText3.image = tkimage6
                diceText3.pack(anchor='c')
            elif "RED FAILURE" in c: #7
                tkimage7= ImageTk.PhotoImage(RedFailure)
                diceText3 = tk.Label(frame2, image=tkimage7)
                diceText3.image = tkimage7
                diceText3.pack(anchor='c')
            elif "RED CRITICAL SUCCESS" in c: #8
                tkimage8= ImageTk.PhotoImage(RedCriticalSuccess)
                diceText3 = tk.Label(frame2, image=tkimage8)
                diceText3.image = tkimage8
                diceText3.pack(anchor='c')

    # slette gamle bilder fra listen og oppdatere med nye
    def clear_frame2():
        for widgets in frame2.winfo_children():
            widgets.destroy()
    clear_frame2()
    frame2.after(10, update_gui)

frame1 = Frame(root)
frame2 = Frame(root)
root.title("vmDice")

text = tk.Label(frame1,text="vmdices:")
text.pack()

# Opprette input-felt for antall svarte terninger
black_amount_label = tk.Label(frame1, text="Antall svarte terninger:")
black_amount_label.pack()
black_amount_entry = tk.Entry(frame1)
black_amount_entry.pack()

# Opprette input-felt for antall røde terninger
red_amount_label = tk.Label(frame1, text="Antall røde terninger:")
red_amount_label.pack()
red_amount_entry = tk.Entry(frame1)
red_amount_entry.pack()

# Opprette knapp for å rulle terninger
roll_button = tk.Button(text="Rull terninger", command=roll_dice)
roll_button.pack()

frame1.pack(padx=1,pady=1)
frame2.pack(padx=10,pady=10)

root.mainloop()