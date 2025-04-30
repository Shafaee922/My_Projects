print("Welcome to the love calculator!")
name_1 = input("Enter your nice name: ").lower()
name_2 = input("Enter his / her nice name: ").lower()

combined_name = name_1 + name_2

# true 
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
true = t + r + u + e

# love
l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")
love = l + o + v + e

score = int(str(true) + str(love))

if score < 10 or score >= 90:
    print(f"Your score is %{score}, You go together like coke and mantoes.")
elif score >= 40 and score <= 50:
    print(f"Your score is %{score}, You are alright together.")
else:
    print(f"Your score is %{score}")
