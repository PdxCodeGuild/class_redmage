
ask_distance = float(input('What is the Distance You would like To Convert? > '))
ask_start_units = input('Enter Which Unit You Would Like To Convert miles, meters, kilometers? > ')
ask_end_units = input('Enter Which Unit You Would Like To Convert miles, meters, kilometers? > ')
ask_units = ask_units.lower()

#Convert Into Meters
convert_Meters = ask_feet * .3048
convert_Miles =  ask_feet * 0.000189394
convert_Kilometers =  ask_feet * 0.0003048
convert_Inches = ask_feet * .0254
convert_Yards = ask_feet * .9114

#Take Values And COvnert Into Meters First
change_to_Meters = ask_distance

if ask_units == 'miles':
    print(f'You have {convert_Miles} Meters)
if ask_units == 'meters':
    print(f'You have {convert_Meters} Meters)
if ask_units == 'kilometers':
    print(f'You have {convert_Kilometers} Meters)
if ask_units == 'inches:
    print(f'You have {convert_Inches} Meters)
if ask_units == 'yards':
    print(f'You have {convert_Yards} Meters)

