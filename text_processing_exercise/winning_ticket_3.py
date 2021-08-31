input_string = input().split(",")

for i in range(len(input_string)):
    current_el = input_string[i]
    input_string.remove(current_el)
    current_el = current_el.strip()
    input_string.insert(i, current_el)
# "@#$^"

special_symbol_at = ["@@@@@@", "@@@@@@@", "@@@@@@@@", "@@@@@@@@@", "@@@@@@@@@@"]
special_symbol_hash = ["######", "#######", "########", "#########", "##########"]
special_symbol_dollar = ["$$$$$$", "$$$$$$$", "$$$$$$$$", "$$$$$$$$$", "$$$$$$$$$$"]
special_symbol_circumflex = ["^^^^^^", "^^^^^^^", "^^^^^^^^", "^^^^^^^^^", "^^^^^^^^^^"]

match_symbol_left = ""
match_symbol_right = ""

for i in range(len(input_string)):
    current_ticket = input_string[i]

    if len(current_ticket) < 20 or len(current_ticket) > 20:
        print("invalid ticket")
        continue

    # for j in range(len(current_ticket)):
    half_size = 10
    left_part = current_ticket[:10]
    right_part = current_ticket[10:]

    for g in range(len(special_symbol_at)):

        winning_combo_at = special_symbol_at[g]
        winning_combo_hash = special_symbol_hash[g]
        winning_combo_dollar = special_symbol_dollar[g]
        winning_combo_circumflex = special_symbol_circumflex[g]


        if winning_combo_at in left_part:
            match_symbol_left = '@'
            lenth_win_string_left = len(winning_combo_at)
        elif winning_combo_hash in left_part:
            match_symbol_left = '#'
            lenth_win_string_left = len(winning_combo_at)
        elif winning_combo_dollar in left_part:
            match_symbol_left = '$'
            lenth_win_string_left = len(winning_combo_at)
        elif winning_combo_circumflex in left_part:
            match_symbol_left = '^'
            lenth_win_string_left = len(winning_combo_at)


        if winning_combo_at in left_part:
            match_symbol_right = '@'
            lenth_win_string_right = len(winning_combo_at)
        elif winning_combo_hash in left_part:
            match_symbol_right = '#'
            lenth_win_string_right = len(winning_combo_at)
        elif winning_combo_dollar in left_part:
            match_symbol_right = '$'
            lenth_win_string_right = len(winning_combo_at)
        elif winning_combo_circumflex in left_part:
            match_symbol_right = '^'
            lenth_win_string_right = len(winning_combo_at)

    # if lenth_win_string_left < 6 and lenth_win_string_right < 6:
    #     print(f'ticket "{current_ticket}" - no match')




    if match_symbol_left == match_symbol_right and match_symbol_left != "" and match_symbol_right != "":

        lenth_win_stirng = min(lenth_win_string_left, lenth_win_string_right)

        if lenth_win_stirng == 10:
            print(f'ticket "{current_ticket}" - {lenth_win_stirng}{match_symbol_right} Jackpot!')
        elif 6 <= lenth_win_stirng <= 9:
            print(f'ticket "{current_ticket}" - {lenth_win_stirng}{match_symbol_right}')
        else:
            print(f'ticket "{current_ticket}" - no match')
    else:
        print(f'ticket "{current_ticket}" - no match')
