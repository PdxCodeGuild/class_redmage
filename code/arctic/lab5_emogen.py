#Emoticon Generator.py

eyes_list = [';' , ':' , 'B' , 'E']
nose_list = ['>' , '*' , '<' , '-']
mouth_list = [')' , '{' , 'D', '(']
for 1 in range(10):
    eyes = random.choice(eyes_list)
    nose = random.choice(nose_list)
    mouth = random.choice(mouth_list) 

    emoticon = eyes + nose + mouth
    print (emoticon)