import random

computer_picked = []
money_balance = 0
track_num = 1

while track_num < 7:
    computer_pick = random.randint(0,100)
    computer_picked.append(computer_pick)
    track_num += 1
    print(computer_picked)