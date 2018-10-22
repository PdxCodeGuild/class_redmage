import random

def lottery_picks():
    picked = []
    for pick in range(7):
        picked.append(random.randint(0, 100))
    return picked

def lottery_wins(x, y):
    wins = 0
    for counter, value in
        if enumlist1[test_num] == enumlist2[test_num]:
            print('you won')
            wins += 1
        else:
            print('you loose')

    return wins


lottery_won = 0

for tries in range(10000):
    userPicked = lottery_picks()
    computerPicked = lottery_picks()
    lottery_won += lottery_wins(userPicked, computerPicked)


print(lottery_won)