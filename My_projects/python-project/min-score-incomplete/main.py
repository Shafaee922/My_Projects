print("Welcome to the Lowest Score Calaulator!")
student_scores = input("Enter a list student scores: ").split()
print(student_scores)
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    lowest_score = student_scores[0]
    if student_scores[n] < lowest_score:
        lowest_score = student_scores[n]


    print(f"The lowest score in the class is {lowest_score}")