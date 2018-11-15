import random

card_name = ["ace","2","3","4","5","6","7","8","9","10","jack","queen","king"]
card_value = [1,2,3,4,5,6,7,8,9,10,10,10,10]

x = random.choice(range(0,13))
y = random.choice(range(0,13))
z = random.choice(range(0,13))

# print(f"x:{x}")
# print(f"y:{y}")
# print(f"z:{z}")

def deal():
    a = card_name[x]
    b = card_name[y]
    c = card_name[z]
    return f"{a} {b} {c}"

print(f"Your three cards are: {deal()}") 

def hand_value():
    a = card_value[x] + card_value[y] + card_value[z]
    return a

print(f"\nYour hand value is: {hand_value()}\n")

if hand_value() > 21:
    print("Bust!")
elif hand_value() == 21:
    print("Blackjack!")
elif hand_value() < 21 and hand_value() >=16:
    print("Stay!")
elif hand_value() <21 and hand_value() < 16:
    print("Hit!")

