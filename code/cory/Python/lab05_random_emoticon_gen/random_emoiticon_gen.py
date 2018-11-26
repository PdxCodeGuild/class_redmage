# Version 2
import random
eyes_list = [':', '8', ';']
nose_list = ['^', '-', '{']
mouth_list = [')', '(', 'D']

for x in range(5):
    out_string = ''
    out_string += random.choice(eyes_list)
    out_string += random.choice(nose_list)
    out_string += random.choice(mouth_list)
    print(out_string, end = '\t')