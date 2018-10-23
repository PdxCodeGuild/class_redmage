import random, time

# Tracks How Much Money Is Earned
money_balance = 0
# Set Variable To Be Used In For num2 loop
wins = 0
# Set Variable To Call ifwon function
returned_win_won = ()
# How Many Times The Game Was Played
counter = 0

# Function To Pick Both The User and COmputer TIckets
def get_choices():
    picked = []
    for _ in range(7):
        pick = random.randint(0, 100)
        picked.append(pick)
    return picked

#Function To Calculate Wins
def money_calc(wins):
    money_balance = 0
    if wins == 0:
        money_balance -= 1
    elif wins == 1:
        money_balance += 4
    elif wins == 2:
        money_balance += 7
    elif wins == 3:
        money_balance += 100
    elif wins == 4:
        money_balance += 50000
        print('You Won Big $50k')
        print(user_picked)
        print(computer_picked)
    elif wins == 5:
        money_balance += 1000000
        print('You Won Big $100k')
        print(user_picked)
        print(computer_picked)
    elif wins == 6:
        money_balance += 25000000
        print('You Won Big $25 MILLON')
        input('Paused You Won The Jackpot'))
        print
        print(user_picked(computer_picked)
    return money_balance

# Function To See If There Are Any Winning Tickets
def ifwon(user_picked, computer_picked):
    wins = 0
    money_won = 0
    return_win_won = ()
    for index in range(7):
        if computer_picked[index] == user_picked[index]:
            wins += 1
        money_won = (money_calc(wins))
        return_win_won = wins, money_won
    return return_win_won


# Loop To Random Pick User Ticket and Random Pick COmputer Ticket
for num2 in range(1000000000):
    computer_picked = get_choices()
    user_picked = get_choices()
    returned_win_won = ifwon(user_picked, computer_picked)
    returned_win_won = list(returned_win_won)
    counter += 1
    wins += returned_win_won[0]
    money_balance += returned_win_won[1]
    f = open("/var/www/lottery_python/Lottery_Results.txt", "w+")
    f.write(f"You won {wins} Times "
            f"\nYou Now Have {money_balance} Dollars Total Money"
            f"\nYou Have Played {counter} Many Times"
            f"\nYour Average Win Rate is {money_balance / counter}")

    f.close()






print(f'You Won {wins} Times')
print(f'You Now Have {money_balance} Dollars Total Money')
print(f'You Have Played {counter} Many Times')
print(f'Your Average is Win Rate is {money_balance / counter} ')


<<<<<<< HEAD
def computer_choices(computer_picked):
    track_num = 1
    while track_num < 7:
        computer_pick = random.randint(0,100)
        computer_picked.append(computer_pick)
        track_num += 1
        if track_num == 7:
            return computer_picked

def user_choices(user_picked):
    track_num = 1
    while track_num < 7:
        user_pick = random.randint(0,100)
        user_picked.append(user_pick)
        track_num += 1
        if track_num == 7:
            return user_picked

def ifwon(user_picked, computer_picked, wins):
    if computer_picked[0] == user_picked[0]:
        wins += 2
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


x = 0

while x < 10000000:
    print(user_choices(user_picked))
    print(computer_choices(computer_picked))
    print(ifwon(user_picked, computer_picked, wins))
    x += 1

print(f'You Won {wins} Times!!!')
=======
>>>>>>> b2e7b67c556a0613e76ae9ca4d0b12daf2cdb8c3


    