import tkinter as tk
from tkinter import messagebox
import random

def check_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    result = check_winner(player_choice, computer_choice)

    messagebox.showinfo("Result", f"Computer chose {computer_choice}\n{result}")

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

label = tk.Label(root, text="Select your move:")
label.pack(pady=10)

rock_button = tk.Button(root, text="Rock", command=lambda: play_game("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", command=lambda: play_game("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("Scissors"))
scissors_button.pack(pady=5)

root.mainloop()
