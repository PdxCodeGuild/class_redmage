import random


#money_balance = 0
wins = 0

def get_choices():
    picked = []
    for _ in range(7):
        pick = random.randint(0, 100)
        picked.append(pick)
    return picked


#after each wins it starts over and doesnt go up in value
def ifwon(user_picked, computer_picked):
    wins = 0
    if computer_picked[0] == user_picked[0]:
        wins += 1
    if computer_picked[1] == user_picked[1]:
        wins += 1
    if computer_picked[2] == user_picked[2]:
        wins += 1
    if computer_picked[3] == user_picked[3]:
        wins += 1
    if computer_picked[4] == user_picked[4]:
        wins += 1
    if computer_picked[5] == user_picked[5]:
        wins += 1
    return wins



# why does my lists get appended when if i dont clear them at the end of this loop?
for num in range(1000):
    computer_picked = get_choices()
    user_picked = get_choices()
    print(computer_picked)
    print(user_picked)
    #user_picked = []
    #print(user_choices(user_picked))
    #im calling the function ifwon and expecting it to return wins, pass it back and save as "won"
    wins += ifwon(user_picked, computer_picked)
#    user_picked = []
#    computer_picked = []


print('You won ' + str(wins) + ' Times')





    