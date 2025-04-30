print("Welcome to the Even Number Calculator!")
total = 0
for i in range(0, 101):
    if i % 2 == 0:
        total += i
print(f"The total number is {total}")