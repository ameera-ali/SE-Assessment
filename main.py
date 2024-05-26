import tkinter
import tkinter as tk
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz import quiz_data

win = tk.Tk()

# Fonts
style1= font.Font(family='Helvetica', size=25, weight='bold')
style2 = font.Font(family='Helvetica', size=20)

win.grid_rowconfigure(0, weight=1)
win.grid_columnconfigure(0, weight=1)

#Welcome Page:
welcome_pg = Frame(win)
welcome_pg.grid(row=0, column=0, sticky="nsew")

welcome_pg.grid_rowconfigure(0, weight=1)
welcome_pg.grid_rowconfigure(1, weight=1)
welcome_pg.grid_columnconfigure(0, weight=1)
welcome_pg.configure(bg='#E6E6FA')


welcome_lb = Label(welcome_pg, text="Recognising Types of Triangles", font=style1)
welcome_lb.configure(bg='#E6E6FA')
welcome_lb.pack(pady=20)

welcome_btn=Button(welcome_pg, text="BEGIN", command=lambda: options_pg.tkraise(), font=style2)
welcome_btn.configure(bg="#E6E6FA")
welcome_btn.pack()

#Options Page: 
options_pg = Frame(win)
options_pg.grid(row=0, column=0, sticky="nsew")

options_pg.grid_rowconfigure(0, weight=1)
options_pg.grid_rowconfigure(1, weight=1)
options_pg.grid_columnconfigure(0, weight=1)
options_pg.configure(bg='#E6E6FA')

options_lb = Label(options_pg, text="Options", font=style1)
options_lb.configure(bg='#E6E6FA')
options_lb.pack(pady=30)

triangles_btn=Button(options_pg, text="LEARNING TRIANGLES", command=lambda: learning_triangles.tkraise(), font=style2 )
quiz_btn=Button(options_pg, text="TAKE THE QUIZ", command=lambda: quiz_pg.tkraise(), font=style2)
triangles_btn.pack()
quiz_btn.pack()

#Learning Triangles Page:
learning_triangles = Frame(win)
learning_triangles.grid(row=0, column=0, sticky="nsew")

learning_triangles.grid_rowconfigure(0, weight=1)
learning_triangles.grid_rowconfigure(1, weight=1)
learning_triangles.grid_columnconfigure(0, weight=1)
learning_triangles.configure(bg='#E6E6FA')

triangles_lb = Label(learning_triangles, text="Learning Triangles", font=style1)
triangles_lb.configure(bg='#E6E6FA')
triangles_lb.pack(pady=50)

isosceles_btn = Button(learning_triangles, text="Isosceles", command=lambda: isosceles.tkraise(), font=style2)
scalene_btn = Button(learning_triangles, text="Scalene", command=lambda: scalene.tkraise(), font=style2)
equilateral_btn = Button(learning_triangles, text="Equilateral", command=lambda: equilateral.tkraise(), font=style2)
right_btn = Button(learning_triangles, text="Right-Angled", command=lambda: right_angled.tkraise(), font=style2)

back_btn = Button(learning_triangles, text="BACK", command=lambda: options_pg.tkraise(), font=style2 )

isosceles_btn.pack()
scalene_btn.pack()
equilateral_btn.pack()
right_btn.pack()
back_btn.pack()

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

#Quiz Page:
quiz_pg = Frame(win)
quiz_pg.grid(row=0, column=0, sticky="nsew")

#Making the question label
root = tk.Tk()
style= Style(theme="flatly")

# Configure the font size for the question and choice buttons
style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))

qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=10
)

qs_label.pack(pady=10)

#Functions to display the current question and options
def show_question():
    #Get the current question from the quiz file list
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    #Display choices on the buttons
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state='normal')

    #clear the feedback label and disable the next button
    feedback_label.config(text="")
    next_btn.config(state="disabled")

#function to check the selected answer and give feedback
def check_answer(choice):
    #Get the current question from the quiz file list
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    #Checking if the selected choice matches the correct answer
    if selected_choice == question["answer"]:
        #Update the score and display it
        global score
        score += 1 
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!", foreground='green')
    else:
        feedback_label.config(text="Incorrect!", foreground="red")
     
     # Disable all choice buttons and enable the next button
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

def next_question():
    global current_question
    current_question +=1

    if current_question < len(quiz_data):
        #if there's more questions, show the next one
        show_question()
    else:
        #if all questions have been answered, display the final score
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score:",format(score,len(quiz_data)))
        root.destroy()


choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

#Making the feedback label
feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

#Initialise the score
score = 0

#Create the score label
score_label = ttk.Label(
    root,
    text="Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

#Making the next button
next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled" 
)
next_btn.pack(pady=10)

#Current question index
current_question = 0

#Show the first question
show_question()

# Start the main event loop
root.mainloop()


quiz_pg.grid_rowconfigure(0, weight=1)
quiz_pg.grid_rowconfigure(1, weight=1)
quiz_pg.grid_columnconfigure(0, weight=1)
quiz_pg.configure(bg='#E6E6FA')

quiz_lb = Label(quiz_pg, text="The Quiz", font=style1)
quiz_lb.configure(bg='#E6E6FA')
quiz_lb.pack()

back_btn6 = Button(quiz_pg, text="BACK", command=lambda: options_pg.tkraise(), font=style2 )
back_btn6.pack()


welcome_pg.tkraise()
win.geometry("600x750")
win.title("Recognising Types of Triangles")
win.resizable(False,False)
win.mainloop()