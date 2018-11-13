#dice game w/ counter
import random 
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
