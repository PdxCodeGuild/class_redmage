#unit_conversion.py
while True:
    to_meters = {"inch": .0254, "ft": .3048, "yd": .9144, "m": 1, "km": 1000, "mi": 1609.34}
    
    user_distance = float(input("What is the distance? > "))
    
    distance_input = ''
    while distance_input not in to_meters.keys():
        distance_input = input("What are the input units? (inch, ft, yd, m, km, mi) > ")

    distance_output = ''
    while distance_output not in to_meters.keys():
        distance_output = input("What are the output units? (inch, ft, yd, m, km, mi) > ")
    
    print(f"{user_distance} {distance_input} is {round((user_distance * to_meters[distance_input] / to_meters[distance_output]), 4)} {distance_output}.")