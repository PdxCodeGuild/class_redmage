#8ball.py - making a magic 8-ball

# importing random to make a random response choice later
import random

# possible responses to the questions
responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely", "You may rely on it.", "As I see it, yes.", "Most Likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very Doubtful."]
play = "y"
while play == "y":
    # requesting user input
    input("I am a magic 8-Ball! Ask me your question: ")
    # picking a random answer from the responses list
    answer = random.choice(responses)
    # responding with that answer.
    print(answer)
    play = input("Would you like to ask another question(y/n)?")
    if play == "n":
        break