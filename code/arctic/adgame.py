import random

attack_outcomes = ['Player wins!', 'Computer wins!']

def resolve_attack():
    return random.choice(attack_outcomes)

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
player_x = 5
player_y = 5
player_health = 3

# add X number enemies in random locations
for i in range(5):
    enemy_x = random.randint(0, height - 1)
    enemy_y = random.randint(0, width - 1)
    board[enemy_x][enemy_y] = '§'

# add treasure
# for i in range(1):
#     treasure_x = random.randint(0, height - 1)
#     treasure_y = random.randint(0, width - 1)
#     board[treasure_x][treasure_y] = '$'

name = input("What is your name? >")
location = input("Where are you from? >")
print(name  + " from " + location  + ',' + ' Welcome to Adventure Land.')
print(name + ',' + ' The object of the game is to kill all the enemies on the board.')

# loop until the user says 'done' or dies
while True:
    if player_health <=0:
        print("Player has no health, Game Over")
        break
    command = input('what is your command?  Please choose up, down, left, right, or done > ')  # get the command from the user

    if command == 'done':
        print("Game Over, well done! "  + name +  " from " + location)
        break  # exit the game
    elif command == 'left':
        player_y -= 1  # move left
    elif command == 'right':
        player_y += 1  # move right
    elif command == 'up':
        player_x -= 1  # move up
    elif command == 'down':
        player_x += 1  # move down

    # check if the player is on the same space as an enemy
    if board[player_x][player_y] == '§':
        print('you\'ve encountered an enemy!')
        action = input('what will you do? Choose between attack or run  > ' )
        if action == 'attack':
            outcome = resolve_attack()
            print(outcome)
            if outcome == "Player Wins":
                print(name + ", " + 'you\'ve slain the enemy!')
                board[player_x][player_y] = ' '  # remove the enemy from the board
            else:
                print(name + ", " + 'you\'ve lost a hit point!')
                player_health -= 1
        else:
            print(name + ' you hestitated and was slained...')
            print("Game Over!")
            break

            # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_x and j == player_y:
                print('☺', end=' ')
            else:
                print(board[i][j], end =' ')  # otherwise print the board square
        print()
     