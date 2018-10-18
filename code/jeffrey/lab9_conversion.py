import string

user_input = float(input("What is the distance in feet (integers only)? "))

feet_meter = user_input * 0.3048

feet_meter = round(feet_meter,4)

print(str(user_input) + " in feet is " + str(feet_meter) + " in meters!")

print("\nEnd Version 1\n")

to_meters_conversion = {
    'ft' : .3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000,
    'yd' : .9144,
    'in' : .0254,
}

user_dist = float(input("What is the numeric distance? "))
user_unit = str(input("What are the units [ft, mi, m, km, yd, or in]? "))

while user_unit not in to_meters_conversion.keys():
    print("Invalid unit entry; Please type unit type according to unit in following list: what are the units [ft, mi, m, km, yd, or in]")
    user_unit = str(input("What are the units? "))

conversion = user_dist  * to_meters_conversion[user_unit]

print("\nThat's "+ str(conversion) + " m.\n")

print("End version 2 & 3\n")

user_dist = float(input("What is the numeric distance? "))
user_unit = str(input("What are the units [ft, mi, m, km, yd, or in]? "))

while user_unit not in to_meters_conversion.keys():
    print("Invalid unit entry; Please type unit type according to unit in following list: what are the units [ft, mi, m, km, yd, or in]")
    user_unit = str(input("What are the units? "))

user_unit_conv = str(input("what unit would you like to convert to [ft, mi, m, km, yd, or in]? "))
while user_unit_conv not in to_meters_conversion.keys():
    print("Invalid unit entry; Please type unit type according to unit in following list: what are the units [ft, mi, m, km, yd, or in]")
    user_unit_conv = str(input("What are the units? "))


conversion = user_dist  * to_meters_conversion[user_unit]
conv2 = conversion / to_meters_conversion[user_unit_conv]

print("\nYour converted value is {0:.2f}".format(conv2) + " " + user_unit_conv)

# print(str(user_dist) + " " + user_unit + " is "+ str(conv2) + user_unit_conv+"\n")

print("\nEnd version 4!")