import tkinter as tk
import random

def play_game():
    user_choice = user_var.get()
    computer_choice = random.choice(["rock", "paper", "scissors"])

    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result_label.config(text="You win!")
    else:
        result_label.config(text="You lose!")

window = tk.Tk()
window.title("Rock Paper Scissors Game")

window.geometry("400x200")
window.resizable(False,False)

user_var = tk.StringVar(window)
user_var.set("rock")

rock_button = tk.Radiobutton(window, text="Rock",height=2, variable=user_var, value="rock")
rock_button.pack()

paper_button = tk.Radiobutton(window, text="Paper",height=2, variable=user_var, value="paper")
paper_button.pack()

scissors_button = tk.Radiobutton(window, text="Scissors",height=2, variable=user_var, value="scissors")
scissors_button.pack()

play_button = tk.Button(window, text="Play",width=6,height=2, command=play_game)
play_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()