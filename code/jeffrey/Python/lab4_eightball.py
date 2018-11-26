import random

par1 = "It is certain;It is decidedly so;Without a doubt;Yes definitely;You may rely on it;As I see it, yes;Most likely;Outlook good;Yes;Signs point to yes;Reply hazy try again;Ask again later;Better not tell you now;Cannot predict now;Concentrate and ask again;Don't count on it;My reply is no;My sources say no;Outlook not so good;Very doubtful"

my_list = par1.split(";")

# print(my_list)

print("Welcome unsuspecting user!\n")

user_question = input("Ask me a questions and I shall reveal the likeliness; when finished say 'done': \n")

while user_question != "done":
    if user_question != None and user_question[-1] == "?":
        print("My answer:",random.choice(my_list))
        user_question = input("\nAsk me another question; when finished type 'done': \n")
    else:
        print("\nPlease properly ask a question.")
        user_question = input("\nAsk me questions; when finished say 'done': \n")
    
print("\nGodspeed!")