# lab14_pick6.py

import random

# setting balance at zero to buy lottery tickets on credit like a responsible adult
tickets_to_buy = int(input("How many tickets would you like to buy? "))
balance = 0
total_spent = 0

# you're still a winner in my book, but you haven't won the lottery yet.
winner =  False

# function to pick 6 random numbers, 1-99, and append them to a list while ensuring there are no repeating numbers
# pass this funciton a list and it will return it full of 6 random digits
def pick6(fresh_ticket):
    pick_count = 0
    fresh_ticket = []
    while pick_count < 6:
        new_num = random.randint(1, 100)
        if new_num not in fresh_ticket:
            pick_count += 1
            fresh_ticket.append(new_num)               
    return fresh_ticket

# function to check how many matching numbers I got
# pass the winning number list first, your ticket num
def check_winnings(winning_nums, your_nums):
    # blank list to set if num at each spot is a match to winning ticket
    winnings = [0, 0, 0, 0, 0, 0]
    for i in range(0,6):
        if i == your_nums[i]:
            # change 0 in winnings list to a 1
            winnings[i] = 1
    # determining the prize
    prize = 0
    winning_slots = sum(winnings)
    if winning_slots == 6:
        prize = 25000000
        print(f"You won $25,000,000 on ticket {your_nums} with {winning_slots} matching numbers!")
    elif winning_slots == 5:
        prize = 1000000
        print(f"You won $1,000,000 on ticket {your_nums} with {winning_slots} matching numbers!")
    elif winning_slots == 4:
        prize = 50000
        # print(f"You won $50,000 on ticket {your_nums} with {winning_slots} matching numbers!")
    elif winning_slots == 3:
        prize = 100
        # print(f"You won $100 on ticket {your_nums} with {winning_slots} matching numbers!")
    elif winning_slots == 2:
        prize = 7
        # print(f"You won $7 on ticket {your_nums} with {winning_slots} matching numbers!")
    elif winning_slots == 1:
        prize = 4
        # print(f"You won $1 on ticket {your_nums} with {winning_slots} matching number!")
    else:
        prize = 0
    winnings_var = 0
    winnings_var += prize
    return winnings_var


# drawing the winning numbers
winning_ticket = []
winning_ticket = (pick6(winning_ticket))

# buying tickets - tickets_to_buy is user input
prev_tickets = []
tickets_bought = 0
total_won = 0
for i in range(tickets_to_buy):
    new_ticket = []
    new_ticket = pick6(new_ticket)
    prev_tickets.append(new_ticket)
    tickets_bought += 1
    # gambling is expensive
    balance -= 2
    # gotta keep track of the habit
    total_spent += 2
    # check to see how much we won
    if new_ticket == winning_ticket:
        winner = True
        break
    else:
        total_won += check_winnings(winning_ticket, new_ticket)
    # at end of each iteration, use function to append the latest picks to master list

if winner == True:
    print(f"Congratulations, you actually won! You only had to buy {tickets_bought} tickets to do it. You spent {total_spent}, and your total winnings are {total_won}. This brings your final balance to {balance}.")
else:
    print(f"Congratulations, you managed to spend ${total_spent} buying {tickets_bought} tickets. Your total winnings: ${total_won}. This brings your final balance to {balance}.")
