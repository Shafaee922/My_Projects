import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '~', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']

print("Welcome to the PyPassword Generator!")

no_letters = int(input("How many letters do you like in your password: "))
no_numbers = int(input("How many numbers do you like in your password: "))
no_symbols = int(input("How many symbols do you like in your password: "))

randPassword = [] 
for letter in range(0, no_letters):
    randPassword.append(random.choice(letters))

for number in range(0, no_numbers):
    randPassword.append(random.choice(numbers))

for symbol in range(0, no_symbols):
    randPassword.append(random.choice(symbols))

random.shuffle(randPassword)
finl_password = ""
for passwd in randPassword:
    finl_password += passwd
    
print(finl_password)