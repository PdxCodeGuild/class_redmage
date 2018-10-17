#madlib.py
name = input("Give me a name >")

verb = input("Give me a verb >")

food = input("What if your favorite food? >")

music = input("What is your favorite instrument? >")

out_string = ''
out_string = out_string + "Hello, my name is "
out_string = out_string + name + ' and I love to ' + verb + ' with my ' + food + ','
out_string = out_string + ' while playing my ' + music + '.' 
print(out_string)