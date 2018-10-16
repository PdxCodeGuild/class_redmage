import random

print("\nWelcome to the Mad Libs lab. You will be asked for three names, nouns, and verbs. The computer will then choose one of each, and create a random mad lib! Let's get started!\n")

while True:
    name_list = list()
    name_list.append(input("Choose the first name: > "))
    name_list.append(input("Choose the second name: > "))
    name_list.append(input("Choose the third name: > "))

    noun_list = list()
    noun_list.append(input("Choose the first noun (person, place, or thing): > "))
    noun_list.append(input("Choose the second noun (person, place, or thing): > "))
    noun_list.append(input("Choose the third noun (person, place, or thing): > "))

    verb_list = list()
    verb_list.append(input("Choose the first verb: > "))
    verb_list.append(input("Choose the second verb: > "))
    verb_list.append(input("Choose the first third: > "))

    print(f"My name is {random.choice(name_list)}. You killed my {random.choice(noun_list)}. Prepare to {random.choice(verb_list)}.")

    end = input("Would you like to continue? (y/n)? > ")
    end = end.lower()
    if end == 'n':
        print("\nThank you for playing!")
        quit()
    while end != 'y' and end != 'n':
        end = input("You need to choose either 'y' or 'n'. Would you like to continue? (y/n)? > ")
        if end == 'y':
            break
        if end == 'n':
            print("\nThank you for playing!")
            quit()

