import random
import tkinter as tk
target=random.randint(0,10)
retries=0
def function1():
    first_layout()
def function2():
    new_game()
def run_both_functions():
    function1()
    function2()
def first_layout():
    layout1.pack(expand=True)
    layout2.pack_forget()
def second_layout():
    layout1.pack_forget()
    layout2.pack(expand=True)

def update_result(text):
    result.configure(text=text)

def new_game():
    check_button.config(state='normal')
    global target, retries
    target = random.randint(0, 10)
    retries = 0
    update_result(text="Guess a number between 0 and 10.")

def play_game():
    global retries
    choice=int(entry_field.get())
    if choice!=target:
        retries+=1
        result="Wrong guess! Try Again!"
        if choice<target:
            hint="The required number is between {} and 10".format(choice)
        else:
            hint="The required number is between 0 and {}".format(choice)
        result+="\nHINT: " + hint
    else:
        result="Congrats! You guessed the required number in just {} takes!".format(retries)
        check_button.config(state='disabled')
        result+=("\nClick on \"Back\" to return to the menu")
    update_result(result)

window=tk.Tk()
window.config(bg="#002366")
window.title("Number Guessing Game")
window.geometry("600x400")
window.resizable(width=False,height=False)
layout1=tk.Frame()
layout2=tk.Frame()

title=tk.Label(layout1,text='Number Guessing Game',font=("times new roman",24,'bold'),fg='#fccb06',bg='#002366')
title.pack(expand=True)
label=tk.Label(layout1,text='Click on play to start the game',font=("arial",12,'italic'),fg='#fccb06',bg='#002366')
label.pack(fill='both',expand=True)
play_button=tk.Button(layout1,text="Play",font=("Arial",16),bg='#fccb06',command=second_layout,activebackground='#edf7f6')
play_button.pack(side='left',fill='both',expand=True)
exit_button_1=tk.Button(layout1,text="Exit",font=("Arial",16),bg='#fccb06',command=exit,activebackground='#edf7f6')
exit_button_1.pack(side='right',fill='both',expand=True)

result=tk.Label(layout2,text="Guess a number between 0 and 10.",font=("Arial",16,'italic'),bg='#002366',fg='#fccb06')
result.pack(side='top',fill='both',expand=True)
guessed_number = tk.StringVar()
entry_field=tk.Entry(layout2,font=("Arial",16),bg='#edf7f6',textvariable=guessed_number, justify="center")
entry_field.pack(side='top',fill='both',expand=True)
check_button=tk.Button(layout2,text="Check",font=("Arial",16),bg='#fccb06',activebackground='#edf7f6',command=play_game)
check_button.pack(side='top',fill='both',expand=True)
back_button=tk.Button(layout2,text="Back",font=("Arial",16),bg='#fccb06',command=run_both_functions,activebackground='#edf7f6')
back_button.pack(side='left',fill='x',expand=True)
exit_button_2=tk.Button(layout2,text="Exit",font=("Arial",16),bg='#fccb06',command=exit,activebackground='#edf7f6')
exit_button_2.pack(side='right',fill='x',expand=True)

first_layout()
window.mainloop()