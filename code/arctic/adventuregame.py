#Adventure Game
import random

width = 10  
height = 10  

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player position
playerX = 1
playery = 1

# add 4 enemies in random locations
for i in range(4):
    enemyX = random.randint(0, height - 1)
    enemyY = random.randint(0, width - 1)
    board[enemyX][enemyY] = '§'

# loop until the user says 'done' or dies
while True:

    command = input('what is your command? ')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command == 'left':
        playerX -= 1  # move left
    elif command == 'right':
        playerX += 1  # move right
    elif command == 'up':
        playerX -= 1  # move up
    elif command == 'down':
        playerX += 1  # move down

    # check if the player is on the same space as an enemy
    if board[playerX] == '§':
        print('you\'ve encountered an enemy!')
        action = input('what will you do? ')
        if action == 'attack':
            print('you\'ve slain the enemy')
            board[playerX] = ' '  # remove the enemy from the board
        else:
            print('you hestitated and were slain')
            break
            # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == playerX:
                print('☺', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()