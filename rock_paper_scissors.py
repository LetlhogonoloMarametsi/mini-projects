import random

# Variables for the user and the computer
user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

# While loop
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quite.\n").lower()
    if user_input == "q":
        break

    # Checking if the user input is not in here the code should ask to keep typing in
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    # Comparing the users pick to the computers pick
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == computer_pick:
        print("It is a tie go again!")

    else:
        print("You lost!")
        computer_wins += 1

# Print the total wins of the user and the total wins of the computer
print("You won", user_wins, "times in the game, and the computer won", computer_wins, "times in the game.")
print("Thank you for playing, Goodbye!")
