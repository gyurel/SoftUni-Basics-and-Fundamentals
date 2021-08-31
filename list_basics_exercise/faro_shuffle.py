deck_of_cards = input().split()
n = int(input())

half_size = len(deck_of_cards) // 2
left_part = deck_of_cards[:half_size]
right_part = deck_of_cards[half_size:]
new_deck = []

for shuffle in range(n):
    new_deck = []
    for i in range(len(left_part)):
        new_deck.append(left_part[i])
        new_deck.append(right_part[i])
    deck_of_cards = new_deck
    left_part = deck_of_cards[:half_size]
    right_part = deck_of_cards[half_size:]

print(new_deck)
