"""
Lab 3: convert a number grade into a letter grade
"""

letter = ''
plusminus= ''

grade = int(input('what is the number grade? '))
if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
else:
    letter = 'F'

if grade == 100:
    plusminus = ''
elif grade < 60:
    plusminus = ''
elif grade % 10 >= 7:
    plusminus = '+'
elif grade % 10 >= 4:
    plusminus = ''
else:
    plusminus = '-'

print(letter + plusminus)


