import tkinter as tk
from tkinter import font
from tkinter import *
import subprocess
from PIL import Image, ImageTk
from tkinter import PhotoImage
import learning_triangles
import quiz_pg

win = tk.Tk()

# Fonts
style1 = font.Font(family='Helvetica', size=25, weight='bold')
style2 = font.Font(family='Helvetica', size=20)

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
welcome_lb.pack(pady=20)

welcome_btn = tk.Button(welcome_pg, text="BEGIN", command=lambda: options_pg.tkraise(), font=style2)
welcome_btn.configure(bg="#E6E6FA")
welcome_btn.pack(pady=10)

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

triangles_btn = tk.Button(options_pg, text="LEARNING TRIANGLES", command=lambda: learning_triangles.tkraise(), font=style2)
triangles_btn.configure(bg="#E6E6FA")
triangles_btn.pack(pady=10)

quiz_btn = tk.Button(options_pg, text="TAKE THE QUIZ", command=lambda: quiz_pg.tkraise(), font=style2)
quiz_btn.configure(bg="#E6E6FA")
quiz_btn.pack(pady=10)

# Image
img_file = PhotoImage(file="options.png")
img_file = img_file.subsample(1,1)
image = tk.Label(options_pg, image=img_file)
image.pack(side="bottom")

# Back Button
back_btn = tk.Button(options_pg, text='BACK', command=lambda: welcome_pg.tkraise(), font=style2)
back_btn.configure(bg="#E6E6FA")
back_btn.pack(pady=10)

#Function to run the learning_triangles file
def run_learning_triangles():
    win.destroy()
    subprocess.run(['python', 'learning_triangles.py'])

#Function to run the quiz file
def run_quiz_pg():
    win.destroy()
    subprocess.run(['python', 'quiz_pg'])

# Initial page
welcome_pg.tkraise()

# Window settings
win.geometry("600x750")
win.title("Recognising Types of Triangles")
win.resizable(False, False)
win.mainloop()
