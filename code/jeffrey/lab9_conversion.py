user_input = float(input("[F-M] What is the distance in feet? "))

conv_value = user_input * 0.3048

conv_value = round(conv_value,4)

print(str(user_input) + " in feet is " + str(conv_value) + " in meters!")