height = float(input("Enter your hight in 'cm': "))
result = 0
if height >= 120:
    print("You can ride the roller coaster.")
    age = int(input("Enter your age: "))
    if age < 12:
        result += 5
        print("Your ticket is $5")
    elif age <= 18:
        result += 7
        print("Your ticket is $7")
    elif age > 45 and age <= 55:
        print("You have a free ride on us.")
    else:
        result += 12
        print("Your ticket is $12")
    photo = input("Do you want to take photo?: ").lower()
    if photo == "yes":
        print("The photo costs $3")
        result += 3
    elif photo == "no":
        pass
    else:
        print("You have answer correctly.")
    print(f"You have to pay ${result}")
else:
    print("Sorry, You Can't ride roller coaster.")

