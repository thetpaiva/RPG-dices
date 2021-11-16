from tkinter import *
from tkinter import ttk
import random
from typing import ForwardRef

root = Tk()
#Function to count the clicks 
root.counter = 0

def clicked():
    root.counter += 1
    if root.counter > 10:
        for widget in frame.winfo_children():
            widget.destroy()
        root.counter = 1
    return root.counter 

#Variables and Labels position 
dadosLabel = ttk.Label(root, text="Dados")
dadosLabel.grid(row=0, column=1)
modPovLabel = ttk.Label(root, text="Mod +")
modPovLabel.grid(row=0, column=3)
nLabel = ttk.Label(root, text="Nº")
nLabel.grid(row=0, column=0)
modNagLabel = ttk.Label(root, text="Mod -")
modNagLabel.grid(row=0, column=5)

#plus sign (Variables and Labels position)
positiveLable1 = ttk.Label(root, text="+", width=1)
positiveLable1.grid(row=1, column=2)
positiveLable2 = ttk.Label(root, text="+", width=1)
positiveLable2.grid(row=2, column=2)
positiveLable3 = ttk.Label(root, text="+", width=1)
positiveLable3.grid(row=3, column=2)
positiveLable4 = ttk.Label(root, text="+", width=1)
positiveLable4.grid(row=4, column=2)
positiveLable5 = ttk.Label(root, text="+", width=1)
positiveLable5.grid(row=5, column=2)
positiveLable6 = ttk.Label(root, text="+", width=1)
positiveLable6.grid(row=6, column=2)
positiveLable7 = ttk.Label(root, text="+", width=1)
positiveLable7.grid(row=7, column=2)

#Negative sign (Variables and Labels position)
negativeLable1 = ttk.Label(root, text="-", width=1)
negativeLable1.grid(row=1, column=4)
negativeLable2 = ttk.Label(root, text="-", width=1)
negativeLable2.grid(row=2, column=4)
negativeLable3 = ttk.Label(root, text="-", width=1)
negativeLable3.grid(row=3, column=4)
negativeLable4 = ttk.Label(root, text="-", width=1)
negativeLable4.grid(row=4, column=4)
negativeLable5 = ttk.Label(root, text="-", width=1)
negativeLable5.grid(row=5, column=4)
negativeLable6 = ttk.Label(root, text="-", width=1)
negativeLable6.grid(row=6, column=4)
negativeLable7 = ttk.Label(root, text="-", width=1)
negativeLable7.grid(row=7, column=4)

#Function for printing the rolls  
def Results(n, x, listOfResults, mp, mn, diceTotal, c):
    row = 1
    diceResults = "{}: ({}d{} = {}) + {} - {} = {}".format(c,n, x, listOfResults, mp, mn, diceTotal)
    diceResultsLabel = ttk.Label(frame, text=diceResults)
    diceResultsLabel.grid(row= c, column=0)

#function for the dice results
def dice(x, n, mp, mn, c):
    diceTotal = 0
    listOfResults = ""
    if mn == '':
        mn = 0
    if mp == '':
        mp = 0
    if n == '':
        diceTotal = random.randint(1, x) + int(mp) - int(mn)
        listOfResults = "{} +".format(diceTotal)
    else:
        for _ in range(int(n)):
            diceRoll = random.randint(1, x)
            diceTotal += diceRoll
            results = "{} +".format(diceRoll)
            listOfResults += results
        diceTotal += int(mp) - int(mn)
    Results(n, x, listOfResults, mp, mn, diceTotal, c)

    


#Variables of the Textbox (positive modifiers)
d4_modPov = ttk.Entry(root, width=2)
d6_modPov = ttk.Entry(root, width=2)
d8_modPov = ttk.Entry(root, width=2)
d10_modPov = ttk.Entry(root, width=2)
d12_modPov = ttk.Entry(root, width=2)
d20_modPov = ttk.Entry(root, width=2)
d100_modPov = ttk.Entry(root, width=2)

#Variaveis of the Textbox (negative modifiers)
d4_modNag = ttk.Entry(root, width=2)
d6_modNag = ttk.Entry(root, width=2)
d8_modNag = ttk.Entry(root, width=2)
d10_modNag = ttk.Entry(root, width=2)
d12_modNag = ttk.Entry(root, width=2)
d20_modNag = ttk.Entry(root, width=2)
d100_modNag = ttk.Entry(root, width=2)

# variables of the dice buttons 
d4 = ttk.Button(root, text="d4", command= lambda: dice(4, d4_n.get(), d4_modPov.get(), d4_modNag.get(), clicked()))
d6 = ttk.Button(root, text="d6", command= lambda: dice(6, d6_n.get(), d6_modPov.get(), d6_modNag.get(), clicked()))
d8 = ttk.Button(root, text="d8", command= lambda: dice(8, d8_n.get(), d8_modPov.get(), d8_modNag.get(), clicked()))
d10 = ttk.Button(root, text="d10", command= lambda: dice(10, d10_n.get(), d10_modPov.get(), d10_modNag.get(), clicked()))
d12 = ttk.Button(root, text="d12", command= lambda: dice(12, d12_n.get(), d12_modPov.get(), d12_modNag.get(), clicked()))
d20 = ttk.Button(root, text="d20", command= lambda: dice(20, d20_n.get(), d20_modPov.get(), d20_modNag.get(), clicked()))
d100 = ttk.Button(root, text="d100", command= lambda: dice(100, d100_n.get(), d100_modPov.get(), d100_modNag.get(), clicked()))

#Variables of the quantity of dices 
d4_n = ttk.Combobox(root, values=('1','2','3','4','5','6','7','8','9','10'), width=1)
d6_n = ttk.Combobox(root, values=('1','2','3','4','5','6','7','8','9','10'), width=1)
d8_n = ttk.Combobox(root, values=('1','2','3','4','5','6','7','8','9','10'), width=1)
d10_n = ttk.Combobox(root, values=('1','2','3','4','5','6','7','8','9','10'), width=1)
d12_n = ttk.Combobox(root, values=('1','2','3','4','5','6','7','8','9','10'), width=1)
d20_n = ttk.Combobox(root, values=('1','2','3','4','5','6','7','8','9','10'), width=1)
d100_n = ttk.Combobox(root, values=('1','2','3','4','5','6','7','8','9','10'), width=1)

#Position of the ComboBox
d4_n.grid(row = 1, column = 0)
d6_n.grid(row = 2, column = 0)
d8_n.grid(row = 3, column = 0)
d10_n.grid(row = 4, column = 0)
d12_n.grid(row = 5, column = 0)
d20_n.grid(row = 6, column = 0)
d100_n.grid(row = 7, column = 0)

#Position of the buttons  
d4.grid(row=1, column=1)
d6.grid(row=2, column=1)
d8.grid(row=3, column=1)
d10.grid(row=4, column=1)
d12.grid(row=5, column=1)
d20.grid(row=6, column=1)
d100.grid(row=7, column=1)

#Postion of the Textbox (positive modifiers)
d4_modPov.grid(row=1, column=3)
d6_modPov.grid(row=2, column=3)
d8_modPov.grid(row=3, column=3)
d10_modPov.grid(row=4, column=3)
d12_modPov.grid(row=5, column=3)
d20_modPov.grid(row=6, column=3)
d100_modPov.grid(row=7, column=3)

#Postion of the Textbox (positive modifiers)
d4_modNag.grid(row=1, column=5)
d6_modNag.grid(row=2, column=5)
d8_modNag.grid(row=3, column=5)
d10_modNag.grid(row=4, column=5)
d12_modNag.grid(row=5, column=5)
d20_modNag.grid(row=6, column=5)
d100_modNag.grid(row=7, column=5)

#Frame of the rolls history
frame = ttk.Frame(root, borderwidth=5, relief='ridge', height=225, width=200)
frame.grid(row=8, column=0, columnspan=6, rowspan=2)
frame.grid_propagate(0)
historyLabel = ttk.Label(frame, text="Roll History: ")
historyLabel.grid(row=0, column=0)

#Mainloop
root.mainloop()