#lab9_unitconv.py

# Setting up a conversion to and from meters, which will serve as the base unit for all conversions.
meters_dict = {"in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.34, "m": 1, "km": 1000}

# priming
in_count = 0
in_unit = ""
out_unit = ""

# RTFM
print("This is a unit converter. When prompted, please enter the number of units you would like to convert. Then at the second prompt, enter the unit to which you wish to convert in (inches), ft (feet), yd (yards) mi (miles), m (meters), or km (kilometers)")

# making sure the user has input the right stuff
while in_count <= 0:
    in_count = int(input("How many units would you like to convert?>"))
while in_unit not in meters_dict:
    in_unit = input("What's the unit of measurement (in, ft, yd, mi, m, or km)?>")
while out_unit not in meters_dict:
    out_unit = input("To which unit would you like to convert (in, ft, yd, mi, m, or km)?>")

# doing math
out_count = in_count * meters_dict[in_unit] / meters_dict[out_unit]

#printing out the results
print(f"{in_count}{in_unit} is equal to {out_count}{out_unit}")