import random
import string

# Number permission, for number_of_tickets loop
number_permission = list(string.digits)

# Set starting balance
starting_bal = 0

# Set cost of ticket ($2)
ticket_cost = 2

# Set variable to track winnings
winnings = 0

# Total Tickets
total_tickets = 0

# Pick6 function
def ticket_function():
    ticket_function = []
    for num in range(6):
        ticket_function.append(random.randint(1, 99))
    return ticket_function

# Set lottery winning ticket list, and get the length to match up indicies from wining_ticket and your_ticket
winning_ticket = ticket_function()
length_of_ticket = len(winning_ticket)

# Set the main loop
end_flag = False
while end_flag == False:

# First user input, ask how many tickets they want and set permissions.
    loop_flag = True
    while loop_flag:
        number_of_tickets = input("\nHow many tickets would you like to buy? > ")
        for num in number_of_tickets:
            if num not in number_permission:
                print("The program didn't like that answer. Let's try again.")
                break
            else:
                number_of_tickets = int(number_of_tickets)
                loop_flag = False
                break

# Calculates however many tickets you chose, tallies other variables like matching numbers of tickets, total tickets, total spent, total gained, etc.
    for x in range(number_of_tickets):

        matching_nums = 0
        your_ticket = ticket_function()
        print(f"\n{your_ticket}")

        for i in range(length_of_ticket):
            if your_ticket[i] == winning_ticket[i]:
                matching_nums += 1         

        if matching_nums == 1:
            winnings += 4
        elif matching_nums == 2:
            winnings += 7
        elif matching_nums == 3:
            winnings += 100
        elif matching_nums == 4:
            winnings += 50000
        elif matching_nums == 5:
            winnings += 1000000
        elif matching_nums == 6:
            winnings += 25000000

        starting_bal += ticket_cost
        total_tickets += 1

# Show winning ticket. Caculate number of tickets bought, how many winning tickets you have, and show how much you have won (tickets bought - winnings).
    print(f"\n{winning_ticket} was the winning ticket.\n")
    print(f"You have played the lottery {total_tickets} times. It cost ${starting_bal} and you won ${winnings}. Your funds are now ${winnings - starting_bal}. Your return of invenstment is {((winnings - starting_bal) / starting_bal)}.")

# User chooses if they want to play again or quit. 
# If you continue it chooses a new winning ticket. <----------------------------
    loop_flag = True
    while loop_flag:
        end_input = ''
        while end_input != 'y' and end_input != 'n':
            end_input = input("Would you like to play the lottery again? (y/n) > ").lower()
        if end_input == 'n':
            print('\nThank you for playing the lottery! Goodbye!\n')
            loop_flag = False
            end_flag = True
            break
        else:
            winning_ticket = ticket_function()
            loop_flag = False
            break
