kind = ['♦', '♣', '♥', '♠']
value = ['7', '8', '9', '10', 'B', 'D', 'K', 'A']

# a)
deck = [k+v for k in kind for v in value]


# c)
hands = [deck[i:len(deck):4] for i in range(4)]

for hand in hands:
    print(hand)