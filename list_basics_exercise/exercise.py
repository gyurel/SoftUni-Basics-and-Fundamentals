cards_list = input().split()
count = int(input())



for i in range(count):
    cards_1 = cards_list[0:int(len(cards_list) / 2)]
    cards_2 = cards_list[int(len(cards_list) / 2):]
    current_deck = []
    for index in range(len(cards_1)):
        current_deck.append(cards_1[index])
        current_deck.append(cards_2[index])
    cards_list = current_deck



print(cards_list)