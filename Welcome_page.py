import tkinter as tk
from tkinter import *
from tkinter import font

win = tk.Tk()
style1= font.Font(size=25)
style2 = font.Font(size=20)

win.grid_rowconfigure(0, weight=1)
win.grid_columnconfigure(0, weight=1)

#Welcome Page:
welcome_pg = Frame(win)
welcome_pg.grid(row=0, column=0, sticky="nsew")

welcome_pg.grid_rowconfigure(0, weight=1)
welcome_pg.grid_rowconfigure(1, weight=1)
welcome_pg.grid_columnconfigure(0, weight=1)

welcome_lb = Label(welcome_pg, text="Recognising Types of Triangles", font=style1)
welcome_lb.pack(pady=20)

welcome_btn=Button(welcome_pg, text="BEGIN", command=lambda: options_pg.tkraise(), font=style2)
welcome_btn.pack()

#Options Page: 
options_pg = Frame(win)
options_pg.grid(row=0, column=0, sticky="nsew")

options_pg.grid_rowconfigure(0, weight=1)
options_pg.grid_rowconfigure(1, weight=1)
options_pg.grid_columnconfigure(0, weight=1)

options_lb = Label(options_pg, text="Options", font=style1)
options_lb.pack(pady=30)

triangles_btn=Button(options_pg, text="LEARNING TRIANGLES", command=lambda: learning_triangles.tkraise(), font=style2 )
quiz_btn=Button(options_pg, text="TAKE THE QUIZ", command=lambda: quiz_pg.tkraise(), font=style2 )
triangles_btn.pack()
quiz_btn.pack()



#Learning Triangles Page:
learning_triangles = Frame(win)
learning_triangles.grid(row=0, column=0, sticky="nsew")

learning_triangles.grid_rowconfigure(0, weight=1)
learning_triangles.grid_rowconfigure(1, weight=1)
learning_triangles.grid_columnconfigure(0, weight=1)

triangles_lb = Label(learning_triangles, text="Learning Triangles", font=style1)
triangles_lb.pack(pady=50)


back_btn = Button(learning_triangles, text="BACK", command=lambda: options_pg.tkraise(), font=style2 )
isosceles_btn = Button(learning_triangles, text="Isosceles", command=lambda: isosceles.tkraise(), font=style2)
scalene_btn = Button(learning_triangles, text="Scalene", command=lambda: scalene.tkraise(), font=style2)
equilateral_btn = Button(learning_triangles, text="Equilateral", command=lambda: equilateral.tkraise(), font=style2)
right_btn = Button(learning_triangles, text="Right-Angled", command=lambda: right_angled.tkraise(), font=style2)
back_btn.pack()
isosceles_btn.pack()
scalene_btn.pack()
equilateral_btn.pack()
right_btn.pack()

#Isosceles Triangle Page:
isosceles = Frame(win)
isosceles.grid(row=0, column=0, sticky="nsew")

isosceles.grid_rowconfigure(0, weight=1)
isosceles.grid_rowconfigure(1, weight=1)
isosceles.grid_columnconfigure(0, weight=1)

isosceles_lb = Label(isosceles, text="The Isosceles Triangle", font=style1)
isosceles_lb.pack()

back_btn2 = Button(isosceles, text="BACK", command=lambda: learning_triangles.tkraise(), font=style2 )
back_btn2.pack()

#Scalene Triangle Page:
scalene = Frame(win)
scalene.grid(row=0, column=0, sticky="nsew")

scalene.grid_rowconfigure(0, weight=1)
scalene.grid_rowconfigure(1, weight=1)
scalene.grid_columnconfigure(0, weight=1)

scalene_lb = Label(scalene, text="The Scalene Triangle", font=style1)
scalene_lb.pack()

back_btn3 = Button(scalene, text="BACK", command=lambda: learning_triangles.tkraise(), font=style2 )
back_btn3.pack()

#Equilateral Triangle Page:
equilateral = Frame(win)
equilateral.grid(row=0, column=0, sticky="nsew")

equilateral.grid_rowconfigure(0, weight=1)
equilateral.grid_rowconfigure(1, weight=1)
equilateral.grid_columnconfigure(0, weight=1)

equilateral_lb = Label(equilateral, text="The Equilateral Triangle", font=style1)
equilateral_lb.pack()

back_btn4 = Button(equilateral, text="BACK", command=lambda: learning_triangles.tkraise(), font=style2 )
back_btn4.pack()

#Right-Angled Triangle Page:
right_angled = Frame(win)
right_angled.grid(row=0, column=0, sticky="nsew")

right_angled.grid_rowconfigure(0, weight=1)
right_angled.grid_rowconfigure(1, weight=1)
right_angled.grid_columnconfigure(0, weight=1)

right_lb = Label(right_angled, text="The Right-Angled Triangle", font=style1)
right_lb.pack()

back_btn5 = Button(right_angled, text="BACK", command=lambda: learning_triangles.tkraise(), font=style2 )
back_btn5.pack()

#Quiz Page:
quiz_pg = Frame(win)
quiz_pg.grid(row=0, column=0, sticky="nsew")

quiz_pg.grid_rowconfigure(0, weight=1)
quiz_pg.grid_rowconfigure(1, weight=1)
quiz_pg.grid_columnconfigure(0, weight=1)

quiz_lb = Label(quiz_pg, text="The Quiz", font=style1)
quiz_lb.pack()

back_btn6 = Button(quiz_pg, text="BACK", command=lambda: options_pg.tkraise(), font=style2 )
back_btn6.pack()











welcome_pg.tkraise()
win.geometry("600x750")
win.title("Recognising Types of Triangles")
win.resizable(False,False)
win.mainloop()