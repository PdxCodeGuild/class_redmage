# hangman.py

import random
import string

# load list of words
# simple events that will trigger a function> 'correct guess' 'incorrect guess' 'new game' 
# iterate through the list and choose words greater than 5 characters
# choose a word
# produce blanks based on the number of letters in the word chosen for the game
# keep track of guesses
# if a letter is guessed, keep track of it and display it somewhere
# list of 26 blanks, if a letter is guessed, 'move' that letter to its proper place on the blank list

hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


with open('words.txt', 'r+') as f:
    contents = f.read().strip('\n').split('\n')

word_list = []
for i in range(len(contents)-1):
    if len(contents[i]) > 5:
        word_list.append(contents[i])
f.close()

# chooses a random word from the master word list
def new_word():
    game_word = random.choice(word_list)
    game_word = game_word.upper()
    return game_word

# creates a list of blanks, one for each letter in the alphabet
def alphabet_blanks():
    alpha_blanks = []
    for i in alphabet:
        alpha_blanks.append("__")
    return alpha_blanks

# creates a list of blanks, one for each letter in the game word
def new_word_blanks(game_word):
    blanks = []
    for i in game_word:
        blanks.append("__")
    return blanks

# word_blanks = word_blank(game_word)

alphabet = string.ascii_uppercase



# operations to start a fresh game
win = False
loss = False
game_word = new_word()
print(game_word)
word_blanks = new_word_blanks(game_word)
alpha_blanks = alphabet_blanks()
wrong_guesses = 0
letters_guessed = []


# if they have not won or lost yet
while win == False and loss == False:
    print("Welcome to Hangman. Enter 'new' to start a new game. Enter 'quit' at any time to quit.")
    
    user_input = ""

    # making sure the user has entered a single letter.
    while len(user_input) < 1 or len(user_input) > 1 and user_input in alphabet:
        user_input = input("Enter a letter to play. ")
        print(f"letters guessed: {alpha_blanks}")
        print(f"Word: {word_blanks}")
        user_input = user_input.upper()

    # letting the user start a new game
    if user_input == "new":
        game_word = new_word()
        word_blanks = new_word_blanks(game_word)
        alpha_blanks = alphabet_blanks()
        wrong_guesses = 0
        letters_guessed = []
        win = False
        loss = False
        user_input = ""
    
    # letting the user quit
    elif user_input == "quit":
        SystemExit
    # checking for the letter in the game word
    elif user_input in alpha_blanks:
        print("You already guessed that.")
    elif user_input in game_word:
        print(f"Correct. {user_input} is in the word!")
        letters_guessed.append(user_input)
        #adding the letter to the alphabet blanks list
        alpha_index = alphabet.index(user_input)
        alpha_blanks[alpha_index] = user_input
        # adding the letter to the game word blanks list
        for i in range(len(game_word)-1):
            if game_word[i] == user_input:
                word_blanks[i] = user_input
        user_input = ""
        print(alpha_blanks)
        print(word_blanks)
    # user has entered a letter not in the game word
    elif user_input not in game_word:
        wrong_guesses += 1
        print(f"Incorrect. {user_input} is not in the word! You have made {wrong_guesses} incorrect guess(es) out of 6.")
        letters_guessed.append(user_input)

        alpha_index=alphabet.index(user_input)
        alpha_blanks[alpha_index] = user_input
        user_input = ""

    if wrong_guesses == 6:
        loss = True
    elif "__" not in word_blanks:
        win = True
    
if win == True:
    print("You won! Enter 'new' to start a new game or 'quit to quit. ")

elif loss == True:
    print("You lost! Enter 'new' to start a new game or 'quit' to quit.")

    # if correct, append to letters letters_guessed, place into alpha blanks and word blanks
    # if incorrect, appened to letters_guessed, add 1 to wring guesses, wrong_guesses +=1
    

