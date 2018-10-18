
ask_distance = float(input('What is the Distance You would like To Convert? > '))
ask_start_units = input('Enter Which Unit You Would Like To convert FROM: miles, meters, kilometers, feet, inches, yards? > ')
ask_end_units = input('Enter Which Unit You Would Like To convert TO: miles, meters, kilometers, feet, inches, yards? > ')
ask_start_units = ask_start_units.lower()
ask_end_units = ask_end_units.lower()

convert_lib = {'miles': 1609.34, 'meters': 1, 'kilometers':1000, 'feet': 0.3048, 'inches': 0.0254, 'yards': 0.0277778}
convert_lib2 = {'miles': 0.000621371, 'meters': 1, 'kilometers': .001, 'inches': 39.3701, 'yards': 1.09361}

if ask_start_units in convert_lib.keys():
    converted = ask_distance * convert_lib[ask_start_units]
    print(converted)

print(f'The distance of {ask_distance} converted from {ask_start_units} to {ask_end_units} equals {converted * convert_lib2[ask_end_units]}')







