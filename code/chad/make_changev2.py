amount = float(input('Enter A Dollar Amount To Convert? >'))

convert_pennies = ((amount // 1) * 100) + ((amount % 1) * 100)
print(f' You Have {convert_pennies} Total Pennies')

if convert_pennies % 25:
    convert_pennies = convert_pennies % 25
    print(f'You Have {convert_pennies} Quarters')
    convert_pennies = convert_pennies // 25
if convert_pennies % 10:
    print(f'You Have {convert_pennies} Dimes')
    convert_pennies = convert_pennies // 10
if convert_pennies % 5:
    print(f'You Have {convert_pennies} Nickles')
    convert_pennies = convert_pennies // 5
if convert_pennies % 1:
    print(f'You Have {convert_pennies} Pennies')
    convert_pennies = convert_pennies // 1



