grade = int(input("Enter Your Grade Number? > "))

if grade % 10 > 5:
    plusminus = '+'
elif grade % 10 <= 5:
    plusminus = '-'


if grade >= 90 < 100:
    print(f'You Got An "A{plusminus}" Grade')
elif grade >= 80 < 90:
    print(f'You Got An "B{plusminus}" Grade')
elif grade >= 70 < 80:
    print(f'You Got An "C{plusminus}" Grade')
elif grade >= 60 < 70:
    print(f'You Got An "D{plusminus}" Grade')
elif grade < 60:
    print(f'You Got An "F{plusminus}" Grade')
else:
    print('You Typed An Invalid Argument')
