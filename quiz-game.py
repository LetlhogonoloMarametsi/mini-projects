# Firstly welcome the user to the game
# Now as user to enter name here
player = input("Enter your name here please. \n")

# The program should now welcome the user with his or her name
print("Welcome to my quiz game " + player + " !.")

# Divider
print("------------------------------------------------------")

# Ask user if he or her wants to play the game
game = input("Would you like to play the game? \n")

# If the user should say yes the game will continue, and if the user says no the game should quit.
if game.lower() != "yes":
    quit()

print("Okay! Lets begin :D ")

# This is a function for counting the users score on what they got correct
score = 0
# Divider
print("---------------------------------------------------------")
# Questions starts here
print("Question One")

answer = input("What is the national soccer team of South Africa? \n")
if answer.lower() == "bafana bafana":
    print("Correct!!!")
    score += 1
else:
    print("Incorrect!")
print("-----------------------------")

print("Question Two")

answer = input("What is the popular rugby team in Pretoria? \n")
if answer.lower() == "blue bulls":
    print("Correct!!!")
    score += 1
else:
    print("Incorrect!")

print("-----------------------------")

print("Question Three")

answer = input("Most bought VW car in South Africa? \n")
if answer.lower() == "polo":
    print("Correct!!!")
    score += 1
else:
    print("Incorrect!")

print("-----------------------------")

print("Question Four")

answer = input("The largest or biggest cat you find in the South African wild life? \n")
if answer.lower() == "lion":
    print("Correct!!!")
    score += 1
else:
    print("Incorrect!")

# Print out the total score of the user and the percentage out of a 100
print("Thank you for answering our questions. You got " + str(score) + " questions correct")
print("You got " + str((score / 4) * 100) + "% questions correct.")

# Now the project ends here.
