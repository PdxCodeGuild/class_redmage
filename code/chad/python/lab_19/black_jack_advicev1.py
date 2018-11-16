first_card = input('What Is Your First Card? > ')
second_card = input('What Is Your Second Card? > ')
third_card = input('What Is Your Third Card? > ')

deck_cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
deck_value = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

#if first_card or second_card not in deck_cards:
#    print('you picked a invalid card')

add_value = deck_value[first_card] + deck_value[second_card] + deck_value[third_card]
print(add_value)

def give_advice(add_value):
 
    if add_value < 17:
        print('Hit!')
    elif add_value > 17 and add_value <= 20:
        print('Stay!')
    elif add_value is 21:
        print('21 You Won!')
    else:
        print('You Busted!')


give_advice(add_value)

