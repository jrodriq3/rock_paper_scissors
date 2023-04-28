import random
import tkinter as tk
from tkinter import *

<<<<<<< Updated upstream
print("Hello, world!")
=======
# I just edited this file
>>>>>>> Stashed changes

def get_my_input_value():
    computer_move = random.randrange(1, 4)
    if computer_move == 1:
        computer_move = "rock"
    elif computer_move == 2:
        computer_move = "paper"
    elif computer_move == 3:
        computer_move = "scissors"
    my_label2 = Label(screen, text="the computer chose: " + computer_move)
    my_label2.place(relx=0.5, rely=0.7)

    user_choice = var.get()
    if user_choice == computer_move:
        my_label3 = Label(screen, text="draw")
        my_label3.pack()
    elif user_choice == "rock":
        if computer_move == "scissors":
            my_label4 = Label(screen, text="YOU WIN")
            my_label4.pack()
        else:
            my_label5 = Label(screen, text="YOU LOSE")
            my_label5.pack()
    elif user_choice == "paper":
        if computer_move == "rock":
            my_label6 = Label(screen, text="YOU WIN")
            my_label6.pack()
        else:
            my_label7 = Label(screen, text="YOU LOSE")
            my_label7.pack()
    elif user_choice == "scissors":
        if computer_move == "paper":
            my_label8 = Label(screen, text="YOU WIN")
            my_label8.pack()
        else:
            my_label9 = Label(screen, text="YOU LOSE")
            my_label9.pack()
    elif user_choice == "my_secret":
        my_label11 = Label(screen, text="you uncovered my easter egg", bg='blue', fg="white", cursor='')
        my_label11.pack()
    else:
        my_label10 = Label(screen, text="you didnt type in your move correctly, please restart program")
        my_label10.pack()


screen = Tk()
screen.title('rock paper scissors')
screen.geometry("1300x800")
screen.configure(cursor="cross")


my_image = PhotoImage(file="Desktop/catpng.png")
my_label = Label(image=my_image, cursor="clock")
my_label.place(relx=.1, rely=.2)

my_label = Label(screen, text="click rock paper or scissors, then click click", font=("Arial", 25), cursor="heart", padx=20, pady=15,
                 bg="red")
my_label.place(relx=0.5, rely=0.8)

my_button = Button(screen, height=10, width=10, text="click", command=get_my_input_value, cursor="star")
my_button.pack()


var = StringVar()
my_rock_radio = Radiobutton(screen, text="ROCK", variable=var, value="rock")
my_rock_radio.pack(anchor= W)
my_paper_radio = Radiobutton(screen, text="PAPER", variable=var, value='paper')
my_paper_radio.pack(anchor=W)
my_scissors_radio = Radiobutton(screen, text="SCISSORS", variable=var, value='scissors')
my_scissors_radio.pack(anchor=W)

screen.mainloop()

