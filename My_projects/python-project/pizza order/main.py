small = 10
medium = 20
large = 25

final_bill = 0

print("Welcome to Hazaragi Fast Food Cafe.")
size = input("What size pizza do you want?: type 's' for samll, 'm' for medium and 'l' for large: ").lower()
add_pepperoni = input("Do you want to add extra pepperoni?: type 'y' for yes and 'n' for no: ").lower()
add_cheese = input("Do you want some extra cheese: type 'y' for yes and 'n' for no: ").lower()

if size == "s":
    print("Small pizza is $10")
    final_bill += 10
elif size == "m":
    print("Medium pizza is $20")
    final_bill += 20
elif size == "l":
    print("Large pizza is $25")
    final_bill += 25
else:
    print("You have to type the correct letter.")

if add_pepperoni == "y":
    if size == "s":
        print("Extra pepperoni for small pizza is $2")
        final_bill += 2
    elif size == "m" or size == "l":
        print("Extra pepperoni for medium and large pizza is $3")
        final_bill += 3
    else:
        print("You have to type the correct letter.")

if add_cheese == "y":
    print("Extra cheese is $1")
    final_bill += 1
elif add_cheese == "n":
    pass
else:
    print("You have to type the correct letter.")

print(f"Thank you for your purchace and your final bill is ${final_bill}")