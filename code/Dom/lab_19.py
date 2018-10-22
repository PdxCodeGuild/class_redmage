#black jack advice 
def blackjack_adv(x,y,z):
    total = (x + y + z)
    if total < 17:
        print(f"{total} Hit")
    elif total >= 17 and total <21:
        print(f"{total} Stay")
    elif total == 21:
        print(f"{total} Blackjack!")
    elif total > 21:
        print(f"{total} Already Busted")

card_dict = {
    "A" : 1, "2": 2, "3" : 3, "4": 4,
    "5": 5, "6" : 6, "7": 7, "8": 8, 
    "9" : 9, "J": 10, "Q": 10, "K": 10
    }

first_card = card_dict[input("What's your first card?: ")]
second_card = card_dict[input("What's your second card?: ")]
third_card = card_dict[input("What's your third card?: ")]
blackjack_adv(first_card,second_card,third_card)
        