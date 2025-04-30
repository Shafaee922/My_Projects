import random

print("Welcome to the best Rock, Paper and Scissors game!")

com_choice = random.randint(0, 2)

user_choice = int(input("What do you choose? type '0' for rock, '1' for paper and '2' for scissors:\n"))

if user_choice > 2 or user_choice < 0:
    print("You have to type the correct number!")
elif user_choice == 0 and com_choice == 2:
    print(f"Computer choose {com_choice} and You choose {user_choice}, You win!")
elif com_choice == 0 and user_choice == 2:
    print(f"Computer choose {com_choice} and You choose {user_choice}, You lose!")
elif user_choice < com_choice:
    print(f"Computer choose {com_choice} and You choose {user_choice}, You lose!")
elif com_choice < user_choice:
    print(f"Computer choose {com_choice} and You choose {user_choice}, You win!")
elif user_choice == com_choice:
    print(f"Computer choose {com_choice} and You choose {user_choice}, You are a draw!")



