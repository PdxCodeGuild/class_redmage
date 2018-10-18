import random
rps_dict = {"Rock": {"Rock": "Its a tie.", "Paper": "You lose!", "Scissors": "You win!"}, "Paper": {"Rock": "You win!", "Paper": "Its a tie!", "Scissors": "You lose!"}, "Scissors": {"Rock": "You lose!", "Paper": "You win!", "Scissors": "Its a tie."}}

while True:
    # user_choice = input("Choose one: Rock, Paper, or Scissors: > ")
    # computer_choice = random.choice(list(rps_dict.keys()))

    # print(f"You chose {user_choice}. Computer chose {computer_choice}. {rps_dict[user_choice][computer_choice]}")

    end_game = input("Would you like to end the game? (y/n) > ")
    end_game.lower()
    while end_game != 'y' and end_game != 'n':
            end_game = input("You need to choose either 'y' or 'n' to continue. Would you like to end the game? (y/n) > ")
    if end_game == 'y':
        print("Thank you for playing!")
        break