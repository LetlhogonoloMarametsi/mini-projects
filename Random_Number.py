import random

# Generate a random number at range
top_of_range = input("Type in your number:\n")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type in a large number than 0 next time.')
        quit()
else:
    print('Please Type a number next time')
    quit()

random_number = random.randint(0, top_of_range)

# Count our guesses
guesses = 0

# A code that is going to run a user guessing feature
while True:
    guesses += 1
    user_guess = input("Make a guess:\n")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please Type a number next time')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in ", guesses, "guesses")
