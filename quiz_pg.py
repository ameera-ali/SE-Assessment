import tkinter
import tkinter as tk
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_data import quiz_data
import welcome_pg
import subprocess

win = tk.Tk()

style1= font.Font(family='Helvetica', size=25, weight='bold')
style2 = font.Font(family='Helvetica', size=20)

win.grid_rowconfigure(0, weight=1)
win.grid_columnconfigure(0, weight=1)

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

back_btn6 = Button(quiz_pg, text="BACK", command=lambda: welcome_pg.tkraise(), font=style2 )
back_btn6.pack()

# Function to run the welcome_pg file
def run_welcome_pg():
    win.destroy()
    subprocess.run(['python', 'welcome_pg.py'])


welcome_pg.tkraise()
win.geometry("600x750")
win.title("Recognising Types of Triangles")
win.resizable(False,False)
win.mainloop()
