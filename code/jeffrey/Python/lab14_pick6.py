import random

balance = 0

ticket_cost = 2

win_dict = {
    0:0,
    1:4,
    2:7,
    3:100,
    4:50000,
    5:1000000,
    6:25000000
}

win6 = []
tick_pick6 = []

def pickem(list_name):
    while len(list_name) < 7:
        list_name.append(random.randint(0,99))
    return list_name

def get_user_nums():
    pickem(tick_pick6)
    return tick_pick6

def get_win6():
    pickem(win6)
    return win6

# win6 = get_win6()
# tick_pick6 = get_user_nums()

#test if the two lists are working.
# print(win6)
# print(tick_pick6)


win6 = get_win6()

i=0
winnings = []


while i < 100001:
    tick_pick6 = get_user_nums()
    for index in range(7):
        if tick_pick6[index] == win6[index]:
            matches += 1
        else:
            matches = 0
    if matches > 0:
        winnings.append(win_dict[matches])
        i+=1
        tick_pick6 = []
    else:
        i+=1
        tick_pick6 = []
    
# print(winnings)

match1 = (winnings.count(4))*4
match2 = (winnings.count(7))*7
match3 = (winnings.count(100))*100
match4 = (winnings.count(50000))*50000
match5 = (winnings.count(1000000))*1000000
match6 = (winnings.count(25000000))*25000000

win_balance = match1 + match2 + match3 + match4 + match5 + match6

balance = -200000 + win_balance

win6.sort()

print(win6)

print(f"${win_balance}\n")
print(f"${balance}\n")
print(f"ROI: {round((((win_balance - 200000)/win_balance)/100),3)}%")