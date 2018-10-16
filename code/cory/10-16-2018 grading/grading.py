grade = int(input("What grade did you get on your test? > "))
letter = ''
mod = ''

if grade < 60:
    letter = 'F'
elif grade < 70:
    letter = 'D'
elif grade < 80:
    letter = 'C'
elif grade < 90:
    letter = 'B'
else:
    letter = 'A'

if grade == 100:
    mod = '+'
elif grade >= 60 and grade % 10 >= 7:
    mod = '+'
elif grade >= 60 and grade % 10 <= 3:
    mod = '-'

print(f"You got a(n) {letter}{mod} on your test.")
    