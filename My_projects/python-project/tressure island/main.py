print("Welcome to Tressure Island!")
print("Your mission is to find the tressure.")
right_left = input("There is a cross in front of you, Do you want to go right or left: ").lower()
if right_left == "left":
    swim_wait = input("There is a lake in front of you, Do you want to swim or wait: ").lower()
    if swim_wait == "wait":
        doors = input("There are three doors in front of you, Which door you want to choose: 'blue', 'yellow', 'red': ").lower()
        if doors == "yellow":
            print("You win the game!")
        elif doors == "blue" or doors == "red":
            print("You choosed wronge and you lost the game.")
        else:
            print("You have to choose the word correctly.")
    elif swim_wait == "swim":
        print("Game over and you lost.")
    else:
        print("You have to type the word correctly.")
elif right_left == "right":
    print("Game over and you lost.")
else:
    print("You have to type the word correctly.")