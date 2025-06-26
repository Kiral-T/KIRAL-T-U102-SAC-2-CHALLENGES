import random

print("Welcome to a game of Rock, Paper, Scissors!")
name = input("Please enter your name: ")

rock_paper_scissors = ["rock", "paper", "scissors"]
player_choice = input("Choose rock, paper, or scissors: ").lower()
computer_choice = random.choice(rock_paper_scissors)

print("You have chosen:", player_choice)
print("The computer chose:", computer_choice)

if player_choice == computer_choice:
    print("It's a draw!")
elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "paper" and computer_choice == "rock") or \
     (player_choice == "scissors" and computer_choice == "paper"):
    print("Congrats! You've won!")
else:
    print("The computer has won!")