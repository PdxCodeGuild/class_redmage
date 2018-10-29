import string
import math

# Gives us the characters to pop for punctuation
punct = list(string.punctuation)

# Function to remove spaces
def no_spaces(doc_name):
    for i in range((len(doc_name)) - 1, 0, -1):
                if doc_name[i] == " ":
                    doc_name.pop(i)
                elif doc_name[i] == "":
                    doc_name.pop(i)
    return doc_name

# Characters variable, returns var: characters (I got 1169)
with open('gettysburg.txt', 'r') as doc:
    doc_characters = doc.read().split('\n')
    doc_characters = ' '.join(doc_characters)
    doc_characters = list(doc_characters)
    doc_characters.sort()
    doc_characters.reverse()

    # Removes all punctuation
    for punc in punct:
        for i in range((len(doc_characters)) - 1, 0, -1):
            if doc_characters[i] == punc:
                doc_characters.pop(i)

    # Removes all spaces
    doc_characters = no_spaces(doc_characters)

    # Return Variable
    characters = len(doc_characters)
    doc.close()

# Words variable, returns var: words (I got 271)
with open('gettysburg.txt', 'r') as doc:
    doc_words = doc.read().split('\n')
    doc_words = ' '.join(doc_words)
    doc_words = doc_words.replace(":", " ")
    doc_words = doc_words.replace(",", " ")
    doc_words = doc_words.replace(".", " ")
    doc_words = doc_words.replace("-", " ")
    doc_words = doc_words.split(' ')
    doc_words.sort()
    doc_words.reverse()
    
    # Removes all spaces
    doc_words = no_spaces(doc_words)
    
    # Return Variable
    words = len(doc_words)
    doc.close()


# Sentances variable, returns var: sentances (I got 10)
with open('gettysburg.txt', 'r') as doc:
    doc_sentances = doc.read().split('\n')
    doc_sentances = ' '.join(doc_sentances)
    doc_sentances = doc_sentances.split('.')
    doc_sentances.sort()
    doc_sentances.reverse()

    # Removes all spaces
    doc_sentances = no_spaces(doc_sentances)

    # Return Variable
    sentances = len(doc_sentances)
    doc.close()

# ARI forumla, 4.71(characters/words) + .5(words/sentances) - 21.43
ari = 4.71 * (characters/words) + .5 * (words/sentances) - 21.43
if ari < 14:
    ari = math.ceil(ari)
else:
    ari = 14

# ARI Scale dictionary from the lab 
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

# Out string, to compile results
out_string = ''
out_string += f"\nThe ARI for gettysburg-address is {ari}.\n"
out_string += f"This corisponds to the {ari_scale[ari]['grade_level']} level of difficulty.\n"
out_string += f"This is suitable for an average person {ari_scale[ari]['ages']} years old.\n"

# Print results
print(out_string)