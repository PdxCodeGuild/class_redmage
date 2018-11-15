
ask_distance = float(input('What is the Distance You would like To Convert? > '))
ask_start_units = input('Enter Which Unit You Would Like To convert FROM: miles, meters, kilometers, feet, inches, yards? > ')
ask_end_units = input('Enter Which Unit You Would Like To convert TO: miles, meters, kilometers, feet, inches, yards? > ')
ask_start_units = ask_start_units.lower()
ask_end_units = ask_end_units.lower()

#Convert To Meters
if ask_start_units == 'miles':
    converted = ask_distance * 1609.34
elif ask_start_units == 'meters':
    converted = ask_distance * 1
elif ask_start_units == 'kilometers':
    converted = ask_distance * 1000
elif ask_start_units == 'feet':
    converted = ask_distance * .3048
elif ask_start_units == 'inches':
    converted = ask_distance * 0.0254
elif ask_start_units == 'yards':
    converted = ask_distance * 0.9144

if ask_end_units == 'miles':
    converted = converted * 0.000621371
elif ask_end_units == 'meters':
    converted = converted * 1
elif ask_end_units == 'kilometers':
    converted = converted * 0.001
elif ask_end_units == 'feet':
    converted = converted * 3.28084
elif ask_end_units == 'inches':
    converted = converted * 39.3701
elif ask_end_units == 'yards':
    converted = converted * 1.09361


print(converted)

print(f'{ask_distance} {ask_start_units} converted to {ask_end_units} equals {converted}{ask_end_units}')






