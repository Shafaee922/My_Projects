print("Welcome to the Highest Score Calculator!")
student_scores = input("Enter a list of student scores: ").split()
print(student_scores)
hightest_score = 0
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    if student_scores[n] > hightest_score:
        hightest_score = student_scores[n]

print(f"The highest score in the class is {hightest_score}")
