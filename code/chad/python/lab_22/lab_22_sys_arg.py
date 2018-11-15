import string, math, sys

count_empty_list_popped = []
print(len(sys.argv))
if len(sys.argv) < 2:
        print('You Put An Invalid File To Load. Please Try Again...')
        quit()
if len(sys.argv) > 2:
    try:
        with open (sys.argv[1], 'r') as text:
            read_text = text.read()
            text.close()
    except:
        print('You Put An Invalid File To Load. Please Try Again...')
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

#Strip Text of end of sentence punctioation, put in list and return
def get_word_count(read_text):
    read_text = read_text.replace('.', '')
    transtable = str.maketrans('', '', string.punctuation)
    read_text = read_text.translate(transtable)
    read_text = read_text.split(' ')
    #Get rid of new lines \n in list
    for i in range(len(read_text)):
        for text in read_text[i]:
            if '\n' in text:
                read_text[i] = read_text[i].replace('\n', '')
    #Get Rid of empty lists
    for i in range(len(read_text)):
            if i == len(read_text):
                print('you have reached the end of the list')
                break
            if '' == read_text[i]:
                count_empty_list_popped.append(read_text.pop(i))
    return read_text
   
def get_char_count(word_count):
    char_count = ''.join(word_count)
    return char_count

def get_sentences(word_count):
    word_count = word_count.replace('!', '.')
    word_count = word_count.replace('?', '.')
    word_count = word_count.split('.')
    return word_count
    
    

#1. Strip test of end of sentence punctiation, put in list and return
word_count = get_word_count(read_text)
char_count = get_char_count(word_count)
sentence_count = get_sentences(read_text)

# Caclulate Actual Lengeth from above
word_count_length = int(len(word_count))
char_count_length = int(len(char_count))
sent_count_length = int(len(sentence_count))

#Do Math For Print Statemetns
ari_math = (4.71*(char_count_length/word_count_length)) + (.5 *(word_count_length/sent_count_length)-21.43)
ari_round_math = math.ceil(ari_math)

#Print Statements
print(f'The ARI For This Text is {ari_math}')
print(f'The reading level for this text is{ari_scale[ari_round_math]}')
