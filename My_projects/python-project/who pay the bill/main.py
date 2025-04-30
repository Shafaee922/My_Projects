import random

print("Welcome to the Bill Split System!")
names = input("Enter everbody's name seperated by a comma and a space: ").split(", ")

randNum = random.randint(0, len(names) - 1)
randName = names[randNum]

print(f"{randName} is going to pay for the bill.")

