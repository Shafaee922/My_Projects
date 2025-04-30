print("Welcome to the Tressure Map!")

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

print(f"{row1}\n{row2}\n{row3}")

row = int(input("Which row do you selec: "))
col = int(input("Which column do you select: "))

if row == 1 and col == 1:
    row1[0] = "X"
elif row == 1 and col == 2:
    row1[1] = "X"
elif row == 1 and col == 3:
    row1[2] = "X"

elif row == 2 and col == 1:
    row2[0] = "X"
elif row == 2 and col == 2:
    row2[1] = "X"
elif row == 2 and col == 3:
    row2[2] = "X"

elif row == 3 and col == 1:
    row3[0] = "X"
elif row == 3 and col == 2:
    row3[1] = "X"
elif row == 3 and col == 3:
    row3[2] = "X"

else:
    print("You have to choose a number in the range of 1 to 3.")

print(f"{row1}\n{row2}\n{row3}")