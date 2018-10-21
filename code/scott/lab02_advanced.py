#lab2_madlib.py - creating a madlib, but slightly more advanced

# importing random so I can do ranom choice
import random

# getting input from user for the parts of speech to inject into the string later
nouns = input("Enter 2 nouns, separated by commas: ")
verbs = input("Ender 3 present continual verbs, separated by commas: ")
drink1 = input("Enter the name of a drink you like: ")

nounlist = nouns.split(", ")
verblist = verbs.split(", ")


# printing the madlib string with random choices for verbs and nouns.
print(f"{random.choice(verblist)} down the {random.choice(nounlist)}, {random.choice(verblist)} {random.choice(nounlist)}, {random.choice(verblist)} on gin and {drink1}")