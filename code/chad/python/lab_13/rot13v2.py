import string

user_input = input('What Word Would You Like To Encrypt? Please Only Give Letters: > ')
rot_version = int(input('Which Rot Cyper Would You Like To Use?'))

#def rot_version:

#1. Convert the Letters input to a list
def convert_text(letters):
    convert_input_to_list = list(user_input)
    return convert_input_to_list
    print(convert_input_to_list)

#2. Makes The Cypher Based On user input of rot_version 
def cypher(x):
    convert_cypher_to_list = list(string.ascii_letters)
    convert_cypher_to_list_before = convert_cypher_to_list[0:x]
    convert_cypher_to_list_after = convert_cypher_to_list[x:26]
    convert_cypher_to_list_after.extend(convert_cypher_to_list_before)
    return convert_cypher_to_list_after

#3. Converts the letters into cypher based on steps 1 and 2.
def convert_letters(letters, cypher):
    #find index of letters from acsii 
    encypted_list = []
    encrypted_string = []
    ascii_list = list(string.ascii_letters)
   #take letters in input word and get index of cypher
    for i in letters:
        encypted_list.append(ascii_list.index(i))
    print(encypted_list)
    for i in encypted_list:
        encrypted_string.append(cypher[i])
     #Join List into string for output
    final_encrypt = ''.join(encrypted_string)   
    print(final_encrypt)
    
def decrypt_letters(encrypted_word, make_cypher):
    unencrypted_word = []
    for i in encrypted_word:
        decrypting = (string.ascii_letters[make_cypher.index(i)])
        unencrypted_word.append(decrypting)
        join_decryption = ''.join(unencrypted_word)
    return join_decryption
    

#Run Function To Return AS a List
convert_text = convert_text(user_input)
#Run FUnction to Make The Cypher To Be USed
make_cypher = cypher(rot_version)
#print(f'Your Cypher looks like this {make_cypher}')
#convert letters to cypher
convert_letters(convert_text, make_cypher)
#Ask user what you want to dycrypt:
decrypt_word = str(input('What Word WOuld you Like To Decrypt? > '))
#call function to decrypt word
decrypted_word = decrypt_letters(decrypt_word, make_cypher)
#print decryption
print(decrypted_word)