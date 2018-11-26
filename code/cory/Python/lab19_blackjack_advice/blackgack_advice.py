# Create dictionary with number and face-card values (A = 1)
card_dict = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 1
}

# Create function that asks for three cards (_func(card1, card2, card3)_)
def blackjack(first_card, second_card, third_card):
    
    total = card_dict[first_card] + card_dict[second_card] + card_dict[third_card]
    

    return total

while True:
    first_card = input("What is the first card? > ").upper()
    second_card = input("What is the second card? > ").upper()
    third_card = input("What is the third card? > ").upper()

    total = blackjack(first_card, second_card, third_card)

    # If value is less than 17 advise hit
    if total < 17:
        print(f"{total} Hit!")

    # If greater than or equal to 17, but less than 21 stay
    elif total >= 17 and total < 21:
        print(f"{total} Stay!")

    # Exactly 21 is Blackjack!
    elif total == 21:
        print(f"{total} Blackjack!")

    # Over 21 is BUST
    else:
        print(f"{total} BUST!")