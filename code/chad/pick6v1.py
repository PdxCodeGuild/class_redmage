import random, time


money_balance = 0
wins = 0
returned_win_won = ()
counter = 0

def get_choices():
    picked = []
    for _ in range(7):
        pick = random.randint(0, 100)
        picked.append(pick)
    return picked

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
        print('You Won Big 100')
        #input('Paused You Won $100 Jackpot')
    elif wins == 4:
        money_balance += 50000
        print('You Won Big $50k')
        input('Paused You Won $50k Jackpot')

    elif wins == 5:
        money_balance += 1000000
        print('You Won Big $100k')
        input('Paused You Won $100k Jackpot')
    elif wins == 6:
        money_balance += 25000000
        print('You Won Big $25 MILLON')
        input('Paused You Won The Jackpot')
    return money_balance

#Why if i put a 0 in for index does it still work fine?
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



for num2 in range(10000000):
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
            f"\nYour Average is Win Rate is {money_balance / counter}")

    f.close()






print(f'You Won {wins} Times')
print(f'You Now Have {money_balance} Dollars Total Money')
print(f'You Have Played {counter} Many Times')
print(f'Your Average is Win Rate is {money_balance / counter} ')




    