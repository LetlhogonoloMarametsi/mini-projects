# Ask user to enter their information
name = input("Enter your name:\n")
print("Welcome", name, "to the adventure of no place else! Whereby at the end of the game you will win a bag of Gold.")
print("-------------------------------------------------------------------")


# Answer the user and give them options where to go next.
print("You are at the end of the road, it is either you go left or right.")
answer = input("Which direction do you wish to take? Left/Right\n").lower()


print("-------------------------------------------------------------------")
# If statement for decision made by user if they want to go left or right and should lose the game.
if answer == "left":
    answer = input("You have come to a river, you can walk around it or swim across?: Type:swim or walk \n").lower()

    print("------------------------------------------------------------------")
    if answer == "swim":
        print("So you swam across the river and got eaten by a anaconda! You lost the game")
    elif answer == "walk":
        print("You walked for many kilometres, you ran out of water and collapsed, you lost the game.")
    else:
        print("Not a valid option. you lose!")

# If user chose to go right the user should decide if they want to cross or head back
elif answer == "right":
    answer = input(
        "You come to a bridge, it looks like its a bit wobbly, do you want to walk across or head back?: "
        "Type: cross/back\n")
    print("----------------------------------------------------------------------")
    if answer == "cross":
        answer = input(
            "You cross the bridge and you meet a suspicious person, do you talk to the person: Yes/No?\n").lower()

        print("-------------------------------------------------------------------------")
        if answer == "yes":
            print("As you speak to the suspicious person, the person decides to give you gold. You WIN!")
        elif answer == "no":
            print("So you chose to ignore the suspicious person and the person gets offended and robs you. You LOSE!")
        else:
            print("Not a valid option you lose")

    elif answer == "back":
        print("You are back at the starting point you lose!")

else:
    print("Not a valid option. you lose!")
print("----------------------------------------------------------------------------------------------")

print("Thank you for playing the game", name)
