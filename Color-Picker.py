# {Imports}
from tkinter import *

# {Window intialization}
Color_picker = Tk()
Color_picker.geometry("550x300")
Color_picker.title("Goose")

# {Main function}
def generate_color(value):
    red = red_scale.get()
    green = green_scale.get()
    blue = blue_scale.get()
    color = f'#{red:02x}{green:02x}{blue:02x}'
    inverted_color = f'#{255-red:02x}{255-green:02x}{255-blue:02x}'
    label_color.config(bg=color, text=color, fg=inverted_color)
    entry.delete(0, END)
    entry.insert(END, color)
frame_RGB = LabelFrame(text='Choose colors', height=250, width=250)
frame_color = LabelFrame(text='Output color', height=250, width=250)
label_color = Label(frame_color, font=('Impact', 15, 'bold'),
                    height=8, width=16, bg='black', fg='white', text='#000000')
red_scale = Scale(frame_RGB, from_=0, to=255, orient=HORIZONTAL, label='Red',
                  length=200, width=20, fg='red', activebackground='red', command=generate_color)
green_scale = Scale(frame_RGB, from_=0, to=255, orient=HORIZONTAL, label='Green',
                    length=200, width=20, fg='green', activebackground='green', command=generate_color)
blue_scale = Scale(frame_RGB, from_=0, to=255, orient=HORIZONTAL, label='Blue',
                   length=200, width=20, fg='blue', activebackground='blue', command=generate_color)
entry = Entry(frame_color, width=7, font=('Arial', 15, 'bold'), justify=CENTER)

# {Placing}
frame_RGB.place(x=15, y=20)
frame_color.place(x=285, y=20)
label_color.place(x=25, y=15)
red_scale.place(x=15, y=10)
green_scale.place(x=15, y=75)
blue_scale.place(x=15, y=140)
entry.place(x=80, y=180)
Color_picker.mainloop()

# ------------------------------------------------------------
# By Dolor 23.04.2022
# https://github.com/AngelZariel/
# ------------------------------------------------------------
