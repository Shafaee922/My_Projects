print("Welcome to the Average Height Calculator!")
students_height = input("Enter a list of students height: ").split()

total_height = 0
counter = 0
for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])
    total_height += students_height[n]
    counter += 1

average = round(total_height / counter)
print(f"The average height of the studetns is: {average}")