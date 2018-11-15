import string

u_in = input("Enter something to be encoded: \n")

u_in = u_in.lower()

u_in_rot_amount = int(input("How much rould you like to rotate the encoding: "))

def rot13(s):

    og_char_str = string.ascii_lowercase
    char_list = list(og_char_str)
    new_list = []
    char_list.reverse()

    for i in range(len(og_char_str)-u_in_rot_amount-1,-1,-1):
        new_list.append(char_list.pop(i))

    char_list.reverse()
    char_str = ''.join(char_list)
    new_str = ''.join(new_list)    

    translate = new_str + char_str

    print(translate)
    rot_char = lambda c: translate[og_char_str.find(c)] if og_char_str.find(c)>-1 else c

    return ''.join( rot_char(c) for c in s )

print(rot13(u_in))