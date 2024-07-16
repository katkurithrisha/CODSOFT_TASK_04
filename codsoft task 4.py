import tkinter as tk
from tkinter import messagebox
import random


root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("400x400")


user_score = 0
computer_score = 0


def computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, comp_choice):
    global user_score, computer_score
    
    if user_choice == comp_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Scissors" and comp_choice == "Paper") or \
         (user_choice == "Paper" and comp_choice == "Rock"):
        user_score += 1
        result = "You win!"
    else:
        computer_score += 1
        result = "Computer wins!"

    label_result.config(text=f"You chose: {user_choice}\nComputer chose: {comp_choice}\n{result}")
    label_score.config(text=f"User Score: {user_score} | Computer Score: {computer_score}")

def user_choice(choice):
    comp_choice = computer_choice()
    determine_winner(choice, comp_choice)

def play_again():
    label_result.config(text="Make your choice!")
    label_score.config(text=f"User Score: {user_score} | Computer Score: {computer_score}")


label_instructions = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 16))
label_instructions.pack(pady=20)

button_rock = tk.Button(root, text="Rock", font=("Helvetica", 16), command=lambda: user_choice("Rock"))
button_rock.pack(side=tk.LEFT, padx=20)

button_paper = tk.Button(root, text="Paper", font=("Helvetica", 16), command=lambda: user_choice("Paper"))
button_paper.pack(side=tk.LEFT, padx=20)

button_scissors = tk.Button(root, text="Scissors", font=("Helvetica", 16), command=lambda: user_choice("Scissors"))
button_scissors.pack(side=tk.LEFT, padx=20)

label_result = tk.Label(root, text="Make your choice!", font=("Helvetica", 16))
label_result.pack(pady=20)

label_score = tk.Label(root, text=f"User Score: {user_score} | Computer Score: {computer_score}", font=("Helvetica", 16))
label_score.pack(pady=20)

button_play_again = tk.Button(root, text="Play Again", font=("Helvetica", 16), command=play_again)
button_play_again.pack(pady=20)


root.mainloop()
