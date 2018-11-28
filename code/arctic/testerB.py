import random
#create the board
width = 10  
height = 10 


# we'll use a list of list to represent the board
board = [] 
for x in range(height):  
    board.append([])  
    for y in range(width):  
        board[x].append(' ')  

# define the player position
player1 = 1


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
        player1 -= 1  # move left
    elif command == 'right':
        player1 += 1  # move right
    elif command == 'up':
        player1 -= 1  # move up
    elif command == 'down':
        player1 += 1  # move down

    # check if the player is on the same space as an enemy
    if board[player1] == '§':
        print('you\'ve encountered an enemy!')

#dice game w/ counter

Counter = {'Player wins!': 0, 'Computer wins!': 0, 'Tie!': 0}

while Counter['Player wins!'] < 3 and Counter['Computer wins!'] < 3:
#These are the list of dice numbers for the player and computer.
    num1 = [1,2,3,4,5,6]
    
    dice1 = random.choice(num1)
   
    comp1 = random.choice(num1)
   

#This is for the "counter" to determine how many wins are obtained.

#This converts the dice roll into a integar.
    player = int(dice1)
    player1 = str(player)

    comp = int(comp1)
    computer = str(comp)
# Again is defined to  to start the loop.

    print("Player rolls  > " +  player1) 
    print("Enemy rolls  > " +  computer) 

    if int(player1) > int(computer):
        print("Player wins!")
        Counter['Player wins!'] += 1
            
    if int(player1) < int(computer):
        print('Enemy wins!')
        Counter['Computer wins!'] += 1
            
    elif player1 == computer:
        Counter['Tie!'] += 1
        print("Tie!")
    
    if Counter['Player wins!'] == 3:
        print("Player has defeated the Enemy!")
        break
    elif Counter['Computer wins!'] == 3:
        print("Computer has defeated the Player!")
        print("Game Over!")
        break
        # action = input('what will you do? ')
        # if action == 'attack':
        #     print('you\'ve slain the enemy')
        #     board[player1] = ' '  # remove the enemy from the board
        # else:
        #     print('you hestitated and were slain')
        #     break

    # this will print the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player1:
                print('☺', end=' ')
            else:
                print(board[i], end=' ')  
        print()