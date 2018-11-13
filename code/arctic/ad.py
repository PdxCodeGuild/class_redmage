import random

width = 10  # the width of the board
height = 10  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player position
player1 = 4
player2 = 4

# add 4 enemies in random locations
for i in range(5):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = '§'
# for i in range(0):
#     print(name + " from " + location + ',' + "You won the game!")
#     break 

name = input("What is your name? >")
location = input("Where are you from? >")
print(name + " from " + location  + ',' + ' Welcome to Adventure Land.')
print(name + ',' + ' The object of the game is to kill all the enemies on the board.')

# loop until the user says 'done' or dies
while True:

    command = input('what is your command? Please choose a direction  >')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command == 'left':
        player1 += 1  # move left
    elif command == 'right':
        player1 -= 1  # move right
    elif command == 'up':
        player2 += 1  # move up
    elif command == 'down':
        player2 -= 1  # move down

#dice game w/ counter

    # Counter = {'Player wins!': 0, 'Computer wins!': 0, 'Tie!': 0}

    # while Counter['Player wins!'] < 3 and Counter['Computer wins!'] < 3:
    #     num1 = [1,2,3,4,5,6]
    #     dice1 = random.choice(num1)
    #     comp1 = random.choice(num1)

    #     player = int(dice1)
    #     player1 = str(player)

    #     comp = int(comp1)
    #     computer = str(comp)

    # check if the player is on the same space as an enemy
    if board[player1][player2] == '§':
        print('you\'ve encountered an enemy!')
        action = input('what will you do? Please attack or run ')
        if action == 'attack':
            if action == 'attack':
                print('you\'ve slain the enemy')
                board[player1] = ' '  
            # print("Player rolls  > " +  player1) 
            # print("Enemy rolls  > " +  computer) 

            # if int(player1) > int(computer):
            #     print("Player wins!")
            #     Counter['Player wins!'] += 1
                    
            # if int(player1) < int(computer):
            #     print('Enemy wins!')
            #     Counter['Computer wins!'] += 1
                    
            # elif player1 == computer:
            #     Counter['Tie!'] += 1
            #     print("Tie!")
            
            # if Counter['Player wins!'] == 3:
            #     print("Player has defeated the Enemy!")
            #     break
            # elif Counter['Computer wins!'] == 3:
            #     print("Enemy has defeated the Player!")
            #     print("Game Over!")
            #     break
            
                # board[player1][player2] = ' '  

        elif action == 'run':
            print('The enemy blocked you and you died!')
            print('Game Over!')
            break

            # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player1 and j == player2:
                print('☺', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()