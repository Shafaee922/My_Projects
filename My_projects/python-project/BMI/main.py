weight = float(input("Enter your weight in 'kg': "))
height = float(input("Enter your height in 'm': "))
bmi = round(weight / (height ** 2))

if bmi < 18.5:
    print(f"Your BMI is {bmi} and you are underweight.")
elif bmi < 25:
    print(f"You BMI is {bmi} and you have normal weight.")
elif bmi < 30:
    print(f"You BMI is {bmi} and you are over overweight.")
elif bmi < 35:
    print(f"You BMI is {bmi} and you are obese.")
else:
    print(f"You BMI is {bmi} and you are clinically obese.")