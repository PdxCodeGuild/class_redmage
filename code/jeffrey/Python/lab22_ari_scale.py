import math
import string
import os
import sys

def ari_calc(characters,words,sentences):
    score = 4.71*(characters/words) + (.5*(words/sentences))-21.43
    score = math.ceil(score)
    return score 

def printer():
    print("+"*50)
    print(f"The ARI score for {file_name} is: {ari_score}")
    print(f"This corresponds to a {ari_scale[ari_score]['grade_level']} level of difficulty")
    print(f"that is suitable for an average age of {ari_scale[ari_score]['ages']}")
    print("+"*50)
    return


try:
    f = open(sys.argv[1],'r', encoding='utf-8-sig')
    text1 = f
    text = f.read().lower()
    file_name = os.path.basename(sys.argv[1])
    f.close()
except FileNotFoundError:
    print("Oops. This is embarrassing. Want to try to correctly input a file name as the arg in position 1?")
    quit()

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

sentence_punc = [".","!","?"]

# counts all the sentence punctioation and then sums it for # of sentences
for e in sentence_punc:
    sentence1 = text.count(sentence_punc[0])
    sentence2 = text.count(sentence_punc[1])
    sentence3 = text.count(sentence_punc[2])
    sentences = (sentence1) + (sentence2) + (sentence3)
    
words = len(list(text.split()))

remove_space_punc = dict.fromkeys(map(ord, '\n ' + string.punctuation))

hello = text.translate(remove_space_punc)

characters = len(hello)

ari_score = ari_calc(characters,words,sentences)

printer()