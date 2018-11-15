# lab22_ari.py

import sys

ari_scale = {
    1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
    2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
    3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
    4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
    5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
    6: {'ages': '10-11', 'grade_level':    '5th Grade'},
    7: {'ages': '11-12', 'grade_level':    '6th Grade'},
    8: {'ages': '12-13', 'grade_level':    '7th Grade'},
    9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

try:
    user_file = sys.argv[1]
except IndexError:
    user_file = input("You forgot to enter a file to process (python lab22_ari.py 'file_to_process'). Enter the filename to process now > ")

with open(user_file, 'r') as file:
    lines = file.read()
lines = lines.split()
print(lines)

sentence_count = 0
char_count = 0
for i in lines:
    sentence_count += i.count(".")
    i = i.strip(",").strip(".")
    char_count += len(i)

word_count = len(lines)

ari = int(4.71 * (char_count / word_count) + .5 * (word_count/ sentence_count) - 21.43)
if ari < 14:
    ari += 1

ages = ari_scale[ari]["ages"]
grade = ari_scale[ari]["grade_level"]

print(f"The ARI for {user_file} is {ari}.\nThis corresponds to a {grade} level of difficulty\nthat is suitable for an average person {ages} years old.")