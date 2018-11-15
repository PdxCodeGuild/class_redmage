amount = float(input('Enter A Dollar Amount To Convert? >'))

convert_pennies = ((amount // 1) * 100) + ((amount % 1) * 100)
convert_pennies = int(convert_pennies)
print(f' You Have {convert_pennies} Total Pennies')

if convert_pennies // 25 != 0:
    print(f'You Have {convert_pennies // 25} Quarters')
    convert_pennies = convert_pennies - ((convert_pennies // 25) * 25)
if convert_pennies // 10 != 0:
    print(f'You Have {convert_pennies // 10} Dimes')
    convert_pennies = convert_pennies - ((convert_pennies // 10) * 10)
if convert_pennies % 5 != 0:
    print(f'You Have {convert_pennies // 5} Nickles')
    convert_pennies = convert_pennies - ((convert_pennies // 5) * 5)
if convert_pennies:
    print(f'You Have {convert_pennies} Pennies')
