# Version 1 <-------------------------------------------------------------------

# user_distance = int(input("What is the distance in feet? > "))
# meter_ft = .3048
# print(f"{user_distance} is {round((user_distance * meter_ft), 4)} m.")

# Version 2 <-------------------------------------------------------------------

# user_distance = int(input("What is the distance? > "))
# user_unit = input("What is the unit of conversion? (ft, mi, me, km) > ")

# if user_unit == 'ft':
#     meter_conversion = .3048
# elif user_unit == 'mi':
#     meter_conversion = 1609.34
# elif user_unit == 'me':
#     meter_conversion = 1
# elif user_unit == 'km':
#     meter_conversion = 1000

# print(f"{user_distance} {user_unit} is {round((user_distance * meter_conversion), 4)} m.")

# Version 3 <-------------------------------------------------------------------

# user_distance = float(input("What is the distance? > "))
# user_unit = input("What is the unit of conversion? (ft, mi, me, km, yrd, in) > ")

# if user_unit == 'ft':
#     meter_conversion = .3048
# elif user_unit == 'mi':
#     meter_conversion = 1609.34
# elif user_unit == 'me':
#     meter_conversion = 1
# elif user_unit == 'km':
#     meter_conversion = 1000
# elif user_unit == 'yrd':
#     meter_conversion = .9144
# elif user_unit == 'in':
#     meter_conversion = .0254

# print(f"{user_distance} {user_unit} is {round((user_distance * meter_conversion), 4)} m.")

# Version 4 (1.0) <-------------------------------------------------------------

# user_distance = float(input("What is the distance? > "))
# distance_input = input("What are the input units? (ft, mi, me, km, yrd, in) > ")
# distance_output = input("What are the output units? (ft, mi, me, km, yrd, in) > ")

# if distance_input == 'ft':
#     meter_conversion_1 = .3048
# elif distance_input == 'mi':
#     meter_conversion_1 = 1609.34
# elif distance_input == 'me':
#     meter_conversion_1 = 1
# elif distance_input == 'km':
#     meter_conversion_1 = 1000
# elif distance_input == 'yrd':
#     meter_conversion_1 = .9144
# elif distance_input == 'in':
#     meter_conversion_1 = .0254

# if distance_output == 'ft':
#     meter_conversion_2 = .3048
# elif distance_output == 'mi':
#     meter_conversion_2 = 1609.34
# elif distance_output == 'me':
#     meter_conversion_2 = 1
# elif distance_output == 'km':
#     meter_conversion_2 = 1000
# elif distance_output == 'yrd':
#     meter_conversion_2 = .9144
# elif distance_output == 'in':
#     meter_conversion_2 = .0254

# print(f"{user_distance} {distance_input} is {round((user_distance * meter_conversion_1 / meter_conversion_2), 4)} {distance_output}.")

# Version 4 (2.0) <-------------------------------------------------------------

# while True:
#     to_meters = {"ft": .3048, "mi": 1609.34, "me": 1, "km": 1000, "yrd": .9144, "in": .0254}
#     user_distance = float(input("What is the distance? > "))
#     distance_input = input("What are the input units? (ft, mi, me, km, yrd, in) > ")
#     distance_output = input("What are the output units? (ft, mi, me, km, yrd, in) > ")
#     print(f"{user_distance} {distance_input} is {round((user_distance * to_meters[distance_input] / to_meters[distance_output]), 4)} {distance_output}.")

# Version 4 (3.0) <-------------------------------------------------------------

while True:
    to_meters = {"ft": .3048, "mi": 1609.34, "me": 1, "km": 1000, "yrd": .9144, "in": .0254}
    
    user_distance = float(input("What is the distance? > "))
    
    distance_input = ''
    while distance_input not in to_meters.keys():
        distance_input = input("What are the input units? (ft, mi, me, km, yrd, in) > ")

    distance_output = ''
    while distance_output not in to_meters.keys():
        distance_output = input("What are the output units? (ft, mi, me, km, yrd, in) > ")
    
    print(f"{user_distance} {distance_input} is {round((user_distance * to_meters[distance_input] / to_meters[distance_output]), 4)} {distance_output}.")