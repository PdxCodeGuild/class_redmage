#lab3_grading.py - assigning letter grades to percentages

# collecting input from the user as an integer
score = int(input("What was your score on the exam?"))

# setting strings
grade = ""
gradeplus = ""

# determining the letter grade
if score in range(90, 100):
    grade = "A"
elif score in range(80, 89):
    grade = "B"
elif score in range(70,79):
    grade = "C"
elif score in range(60, 69):
    grade = "D"
elif score < 60:
    grade = "F"

# determining if there is the need for a + or -
if score % 10 in range(0, 3):
    gradeplus = "-"
elif score % 10 in range(8, 9):
    gradeplus = "+"

# sending responses, includes catch for A+ not caught by 'gradeplus' determination
if grade == "F":
    print("You have failed!")
elif score == 100:
    print("You got an A+!")
else:
    print(f"Your grade is {grade}{gradeplus}!")
