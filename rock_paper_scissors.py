import random
from tkinter import *

user_choice = ""
def get_my_input_value():
    computer_move = random.randrange(1, 4)
    if computer_move == 1:
        computer_move = "rock"
    elif computer_move == 2:
        computer_move = "paper"
    elif computer_move == 3:
        computer_move = "scissors"
    my_label2 = Label(screen, text="the computer chose: " + computer_move)
    my_label2.pack()


    user_choice = my_entry_box.get()
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
    else:
        my_label10 = Label(screen, text="you didnt type in your move correctly, please restart program")
        my_label10.pack()


    
    

screen = Tk()
screen.geometry("800x400")
screen.configure(bg="black")

my_entry_box = Entry(screen, justify="right")
my_entry_box.pack()

my_label = Label(screen, text="Type rock paper or scissors.", font=("Arial", 25))
my_label.place(x=10, y=11)
my_label.pack()

my_button = Button(screen, height=10, width=10, text="click", command=get_my_input_value)
my_button.place(x=4, y=120)


screen.mainloop()
