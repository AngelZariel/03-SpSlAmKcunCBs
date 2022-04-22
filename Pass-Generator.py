# {Imports}
from tkinter import *
import random

# {Characters list}
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
           "A","B","C","D","E","F","G","H","I","G","K","L","M","n","O","P","Q","R","S","T","U","V","W","X","Y","Z",
           "1","2","3","4","5","6","7","8","9","0",
           "@","#","*","@","#","*","@","#","*"]

# {Generate with 8 symbols}
def start8():
    couts = 0
    b = []
    while couts != 8:
        couts += 1
        c = random.choice(letters)
        b.append(c)
        if couts == 8:
            lk = "{}{}{}{}{}{}{}{}".format(b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7])
            output.delete(0, END)
            output.insert(END, lk)

# {Generate with 8 symbols}
def start16():
    couts = 0
    b = []
    while couts != 16:
        couts += 1
        c = random.choice(letters)
        b.append(c)
        if couts == 16:
            lk = "{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7],b[8],b[9],b[10],b[11],b[12],b[13],b[14],b[15])
            output.delete(0, END)
            output.insert(END, lk)

# {Window creating}
Goose = Tk()
Goose.title('Pass Generator')
Goose.config(bg='black')
Goose.resizable(False,False)


Label1 = Label(text="Password Generator!", bg='black', fg='green2', font="smallestpixel-7 16")
output = Listbox(bg ='black',fg="green2", font="smallestpixel-7 12", width=18, height=1)
b8 = Button(text="Generate with 8 characters", bg='green2',fg='black',command=start8)
b16 = Button(text="Generate with 16 characters",bg='green2',fg='black',command=start16)


Label1.grid(row=2, column=2,columnspan=2)
output.grid(row=3, column=2, columnspan=2)
b8.grid(row=4, column=2)
b16.grid(row=4, column=3)
Goose.mainloop()

# ------------------------------------------------------------
# By Dolor 23.04.2022
# https://github.com/AngelZariel/
# ------------------------------------------------------------
