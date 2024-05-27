import tkinter
import tkinter as tk
from tkinter import *
from tkinter import font
import subprocess
import welcome_pg

win = tk.Tk()

# Fonts
style1 = font.Font(family='Helvetica', size=25, weight='bold')
style2 = font.Font(family='Helvetica', size=20)

win.grid_rowconfigure(0, weight=1)
win.grid_columnconfigure(0, weight=1)

learning_triangles = tk.Frame(win)
learning_triangles.grid(row=0, column=0, sticky="nsew")

learning_triangles.grid_rowconfigure(0, weight=1)
learning_triangles.grid_rowconfigure(1, weight=1)
learning_triangles.grid_columnconfigure(0, weight=1)
learning_triangles.configure(bg='#E6E6FA')

learning_triangles_lb = tk.Label(learning_triangles, text="Learning Triangles", font=style1)
learning_triangles_lb.configure(bg='#E6E6FA')
learning_triangles_lb.pack(pady=50)

isosceles_btn = tk.Button(learning_triangles, text="Isosceles", command=lambda: isosceles.tkraise(), font=style2)
isosceles_btn.configure(bg="#E6E6FA")
isosceles_btn.pack(pady=10)

scalene_btn = tk.Button(learning_triangles, text="Scalene", command=lambda: scalene.tkraise(), font=style2)
scalene_btn.configure(bg="#E6E6FA")
scalene_btn.pack(pady=10)

equilateral_btn = tk.Button(learning_triangles, text="Equilateral", command=lambda: equilateral.tkraise(), font=style2)
equilateral_btn.configure(bg="#E6E6FA")
equilateral_btn.pack(pady=10)


right_btn = tk.Button(learning_triangles, text="Right-Angled", command=lambda: right_angled.tkraise(), font=style2)
right_btn.configure(bg="#E6E6FA")
right_btn.pack(pady=10)


back_btn = tk.Button(learning_triangles, text="BACK", command=lambda: run_welcome_pg(), font=style2)
back_btn.configure(bg="#E6E6FA")
back_btn.pack(pady=10)

# Image 
image_file = PhotoImage(file="learning.png")
image_file = image_file.subsample(1,1)
image = tk.Label(learning_triangles, image=image_file)
image.pack(side="bottom")

# Function to run the welcome_pg file
def run_welcome_pg():
    win.destroy()
    subprocess.run(['python', 'welcome_pg.py'])


#Isosceles Triangle Page:
isosceles = Frame(win)
isosceles.grid(row=0, column=0, sticky="nsew")

isosceles.grid_rowconfigure(0, weight=1)
isosceles.grid_rowconfigure(1, weight=1)
isosceles.grid_columnconfigure(0, weight=1)
isosceles.configure(bg='#E6E6FA')

isosceles_lb = Label(isosceles, text="The Isosceles Triangle", font=style1)
isosceles_lb.configure(bg='#E6E6FA')
isosceles_lb.pack()

back_btn2 = Button(isosceles, text="BACK", command=lambda: learning_triangles.tkraise(), font=style2 )
back_btn2.pack()

#Scalene Triangle Page:
scalene = Frame(win)
scalene.grid(row=0, column=0, sticky="nsew")

scalene.grid_rowconfigure(0, weight=1)
scalene.grid_rowconfigure(1, weight=1)
scalene.grid_columnconfigure(0, weight=1)
scalene.configure(bg='#E6E6FA')

scalene_lb = Label(scalene, text="The Scalene Triangle", font=style1)
scalene_lb.configure(bg='#E6E6FA')
scalene_lb.pack()

back_btn3 = Button(scalene, text="BACK", command=lambda: learning_triangles.tkraise(), font=style2 )
back_btn3.pack()

#Equilateral Triangle Page:
equilateral = Frame(win)
equilateral.grid(row=0, column=0, sticky="nsew")

equilateral.grid_rowconfigure(0, weight=1)
equilateral.grid_rowconfigure(1, weight=1)
equilateral.grid_columnconfigure(0, weight=1)
equilateral.configure(bg='#E6E6FA')

equilateral_lb = Label(equilateral, text="The Equilateral Triangle", font=style1)
equilateral_lb.configure(bg='#E6E6FA')
equilateral_lb.pack()

back_btn4 = Button(equilateral, text="BACK", command=lambda: learning_triangles.tkraise(), font=style2 )
back_btn4.pack()

#Right-Angled Triangle Page:
right_angled = Frame(win)
right_angled.grid(row=0, column=0, sticky="nsew")

right_angled.grid_rowconfigure(0, weight=1)
right_angled.grid_rowconfigure(1, weight=1)
right_angled.grid_columnconfigure(0, weight=1)
right_angled.configure(bg='#E6E6FA')

right_lb = Label(right_angled, text="The Right-Angled Triangle", font=style1)
right_lb.configure(bg='#E6E6FA')
right_lb.pack()

back_btn5 = Button(right_angled, text="BACK", command=lambda: learning_triangles.tkraise(), font=style2 )
back_btn5.pack()

learning_triangles.tkraise()
win.geometry("600x750")
win.title("Recognising Types of Triangles")
win.resizable(False,False)
win.mainloop()