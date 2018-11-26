#lab5_randoemogen.py

#importing random to make random choices later
import random

#creating lists of eyes, noses, and mouths
eyes = [":", ";", "8", "B"]
noses = ["-", ",", "~", "'"]
mouths = [")", "(", "|", "D", "]", "[", "/"]

#while loop to create 5 emoticons
i = 0
while i < 5:
    print(random.choice(eyes) + random.choice(noses) + random.choice(mouths))
    i += 1