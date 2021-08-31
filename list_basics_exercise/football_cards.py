team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

cards = input().split()
terminated = False

for card in cards:
    card = card.split("-")

    team_name = card[0]
    team_player = int(card[1])

    if team_name == "A":
        if team_player in team_a:
            team_a.remove(team_player)
    elif team_name == "B":
        if team_player in team_b:
            team_b.remove(team_player)

    if len(team_a) < 7 or len(team_b) < 7:
        print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
        print("Game was terminated")
        terminated = True
        break

if not terminated:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
