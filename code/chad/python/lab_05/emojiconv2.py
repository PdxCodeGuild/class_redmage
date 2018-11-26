import random
eyes =  [':', ';', '~' ]
noses = ['^', '%', '<', '-', '_']
mouths = ['}', ']', '{', '{', '[']

x = 0

while x < 5:
    print(f'{random.choice(eyes)}{random.choice(noses)}{random.choice(mouths)}')
    x += 1