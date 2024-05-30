import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import *
import subprocess
from ttkbootstrap import Style
from PIL import Image, ImageTk
from tkinter import PhotoImage
import quiz_pg

win = tk.Tk()

# Fonts
style1 = font.Font(family='Arial', size=30, weight='bold')
style2 = font.Font(family='Arial', size=24)
style3 = font.Font(family='Arial', size=20)

# Colours:
colour1= '#C2BBF0'
colour2 = '#E6E6FA'
colour3 = 'BLACK'

win.grid_rowconfigure(0, weight=1)
win.grid_columnconfigure(0, weight=1)

# Welcome Page:
welcome_pg = tk.Frame(win)
welcome_pg.grid(row=0, column=0, sticky="nsew")

welcome_pg.grid_rowconfigure(0, weight=1)
welcome_pg.grid_rowconfigure(1, weight=1)
welcome_pg.grid_columnconfigure(0, weight=1)
welcome_pg.configure(bg='#E6E6FA')

welcome_lb = tk.Label(welcome_pg, text="Recognising Types of Triangles", font=style1)
welcome_lb.configure(bg='#E6E6FA')
welcome_lb.pack(pady=80)

welcome_btn = tk.Button(welcome_pg, foreground='BLACK', background=colour2, activebackground=colour2, activeforeground=colour2, highlightthickness=2, highlightcolor=colour2, cursor = 'hand1', width=13, height=2, highlightbackground= colour1, text="BEGIN", command=lambda: options_pg.tkraise(),font=style2)
welcome_btn.configure(bg="#E6E6FA")
welcome_btn.pack()

image_file = PhotoImage(file="welcome.png")
image_file = image_file.subsample(1,1)
image = tk.Label(welcome_pg, image=image_file)
image.pack(side="bottom")

# Options Page:
options_pg = tk.Frame(win)
options_pg.grid(row=0, column=0, sticky="nsew")

options_pg.grid_rowconfigure(0, weight=1)
options_pg.grid_rowconfigure(1, weight=1)
options_pg.grid_columnconfigure(0, weight=1)
options_pg.configure(bg='#E6E6FA')

options_lb = tk.Label(options_pg, text="Options", font=style1)
options_lb.configure(bg='#E6E6FA')
options_lb.pack(pady=30)

triangles_btn = tk.Button(options_pg, text="LEARNING TRIANGLES", command=lambda: learning_triangles.tkraise(), font=style2, foreground='BLACK', background=colour2, activebackground=colour2, activeforeground=colour2, highlightthickness=2, highlightcolor=colour2, cursor = 'hand1', width=19, height=2, highlightbackground= colour1,)
triangles_btn.configure(bg="#E6E6FA")
triangles_btn.pack(pady=10)

quiz_btn = tk.Button(options_pg, text="TAKE THE QUIZ", command=lambda: run_quiz_pg(), font=style2,foreground='BLACK', background=colour2, activebackground=colour2, activeforeground=colour2, highlightthickness=2, highlightcolor='WHITE', cursor = 'hand1', width=13, height=2, highlightbackground= colour1,)
quiz_btn.configure(bg="#E6E6FA")
quiz_btn.pack(pady=10)

# Image
img_file = PhotoImage(file="options.png")
img_file = img_file.subsample(1,1)
image = tk.Label(options_pg, image=img_file)
image.pack(side="bottom")

# Back Button
back_btn = tk.Button(options_pg, text='BACK', command=lambda: welcome_pg.tkraise(), font=style2, foreground='BLACK', background=colour2, activebackground=colour2, activeforeground=colour2, highlightthickness=2, highlightcolor='WHITE', cursor = 'hand1', width=8, height=2, highlightbackground= colour1,)
back_btn.configure(bg="#E6E6FA")
back_btn.pack(pady=10)

#Function to run the quiz file
def run_quiz_pg():
    win.destroy()
    subprocess.run(['python', 'quiz_pg'])

#Learning Triangles Page:
learning_triangles = tk.Frame(win)
learning_triangles.grid(row=0, column=0, sticky="nsew")

learning_triangles.grid_rowconfigure(0, weight=1)
learning_triangles.grid_rowconfigure(1, weight=1)
learning_triangles.grid_columnconfigure(0, weight=1)
learning_triangles.configure(bg='#E6E6FA')

learning_triangles_lb = tk.Label(learning_triangles, text="Learning Triangles", font=style1)
learning_triangles_lb.configure(bg='#E6E6FA')
learning_triangles_lb.pack(pady=30)

isosceles_btn = tk.Button(learning_triangles, text="Isosceles", command=lambda: isosceles.tkraise(), font=style3, foreground='BLACK', background=colour1, activebackground=colour2, activeforeground=colour2, highlightthickness=2, highlightcolor=colour2, cursor = 'hand1', width=11, height=1, highlightbackground= colour1,)
isosceles_btn.pack(pady=10)

scalene_btn = tk.Button(learning_triangles, text="Scalene", command=lambda: scalene.tkraise(), font=style3, foreground='BLACK', background=colour1, activebackground=colour2, activeforeground=colour2, highlightthickness=2, highlightcolor=colour2, cursor = 'hand1', width=11, height=1, highlightbackground= colour1,)
scalene_btn.configure(bg="#E6E6FA")
scalene_btn.pack(pady=10)

equilateral_btn = tk.Button(learning_triangles, text="Equilateral", command=lambda: equilateral.tkraise(), font=style3, foreground='BLACK', background=colour2, activebackground=colour2, activeforeground=colour2, highlightthickness=2, highlightcolor='WHITE', cursor = 'hand1', width=11, height=1, highlightbackground= colour1,)
equilateral_btn.configure(bg="#E6E6FA")
equilateral_btn.pack(pady=10)


right_btn = tk.Button(learning_triangles, text="Right-Angled", command=lambda: right_angled.tkraise(), font=style3, foreground='BLACK', background=colour2, activebackground=colour2, activeforeground=colour2, highlightthickness=2, highlightcolor='WHITE', cursor = 'hand1', width=11, height=1, highlightbackground= colour1,)
right_btn.configure(bg="#E6E6FA")
right_btn.pack(pady=10)


back_btn = tk.Button(learning_triangles, text="Back", command=lambda: options_pg.tkraise(), font=style3, foreground='BLACK', background=colour2, activebackground=colour2, activeforeground=colour2, highlightthickness=2, highlightcolor='WHITE', cursor = 'hand1', width=11, height=1, highlightbackground= colour1,)
back_btn.configure(bg="#E6E6FA")
back_btn.pack(pady=10)

# Image 
im_file = PhotoImage(file="learning.png")
im_file = im_file.subsample(1,1)
image = tk.Label(learning_triangles, image=im_file)
image.pack(side="bottom")

#Isosceles Triangle Page:
isosceles = Frame(win)
isosceles.grid(row=0, column=0, sticky="nsew")

back_btn2 = Button(isosceles, text="Back", command=lambda: learning_triangles.tkraise(), font=style3, foreground='BLACK', background=colour2, activebackground=colour2, activeforeground=colour2, highlightthickness=2, highlightcolor='WHITE', cursor = 'hand1', width=10, height=1, highlightbackground= colour1)
back_btn2.pack(side="bottom") 

isosceles_img = PhotoImage(file="isosceles.png")
isosceles_img = isosceles_img.subsample(1,1)
image = tk.Label(isosceles, image=isosceles_img)
image.pack()

isosceles.grid_rowconfigure(0, weight=1)
isosceles.grid_rowconfigure(1, weight=1)
isosceles.grid_columnconfigure(0, weight=1)
isosceles.configure(bg='#F8F4FF')

#Scalene Triangle Page:
scalene = Frame(win)
scalene.grid(row=0, column=0, sticky="nsew")

back_btn3 = Button(scalene, text="Back", command=lambda: learning_triangles.tkraise(), font=style3, foreground='BLACK', background=colour2, activebackground=colour2, activeforeground=colour2, highlightthickness=2, highlightcolor='WHITE', cursor = 'hand1', width=10, height=1, highlightbackground= colour1)
back_btn3.pack(side='bottom')

scalene_img = PhotoImage(file="scalene.png")
scalene_img = scalene_img.subsample(1,1)
image = tk.Label(scalene, image=scalene_img)
image.pack()

scalene.grid_rowconfigure(0, weight=1)
scalene.grid_rowconfigure(1, weight=1)
scalene.grid_columnconfigure(0, weight=1)
scalene.configure(bg='#F8F4FF')

#Equilateral Triangle Page:
equilateral = Frame(win)
equilateral.grid(row=0, column=0, sticky="nsew")

back_btn4 = Button(equilateral, text="Back", command=lambda: learning_triangles.tkraise(), font=style3, foreground='BLACK', background=colour2, activebackground=colour2, activeforeground=colour1, highlightthickness=2, highlightcolor='WHITE', cursor = 'hand1', width=10, height=1, highlightbackground= colour1)
back_btn4.pack(side='bottom')

equilateral_img = PhotoImage(file="equilateral.png")
equilateral_img = equilateral_img.subsample(1,1)
image = tk.Label(equilateral, image=equilateral_img)
image.pack()

equilateral.grid_rowconfigure(0, weight=1)
equilateral.grid_rowconfigure(1, weight=1)
equilateral.grid_columnconfigure(0, weight=1)
equilateral.configure(bg='#F8F4FF')


#Right-Angled Triangle Page:
right_angled = Frame(win)
right_angled.grid(row=0, column=0, sticky="nsew")

back_btn5 = Button(right_angled, text="Back", command=lambda: learning_triangles.tkraise(), font=style3, foreground='BLACK', background=colour2, activebackground=colour2, activeforeground=colour1, highlightthickness=2, highlightcolor='WHITE', cursor = 'hand1', width=10, height=1, highlightbackground= colour1)
back_btn5.pack(side='bottom')

right_angled_img = PhotoImage(file="right-angled.png")
right_angled_img = right_angled_img.subsample(1,1)
image = tk.Label(right_angled, image=right_angled_img)
image.pack()

right_angled.grid_rowconfigure(0, weight=1)
right_angled.grid_rowconfigure(1, weight=1)
right_angled.grid_columnconfigure(0, weight=1)
right_angled.configure(bg='#F8F4FF')


# Initial page
welcome_pg.tkraise()

# Window settings
win.geometry("600x750")
win.title("Recognising Types of Triangles")
win.resizable(False, False)
win.mainloop()
