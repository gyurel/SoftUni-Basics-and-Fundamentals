player_pool = {}
players_skills = {}

command = input()

while command != "Season end":

    if " -> " in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)

        if player not in player_pool:
            player_pool[player] = {position: skill}
            players_skills[player] = skill

        elif position not in player_pool[player]:
            player_pool[player][position] = skill
            players_skills[player] += skill
        else:
            if skill > player_pool[player][position]:
                player_pool[player][position] = skill
                players_skills[player] += skill

    elif " vs " in command:
        player1, player2 = command.split(" vs ")

        if player1 in player_pool and player2 in player_pool and player1 != player2:
            for item in player_pool[player1].keys():
                if item in player_pool[player2].keys():
                    if players_skills[player1] > players_skills[player2]:
                        del players_skills[player2]
                        del player_pool[player2]
                    elif players_skills[player1] < players_skills[player2]:
                        del players_skills[player1]
                        del player_pool[player1]

    command = input()

players_skills_sorted = {name: skill for name, skill in sorted(players_skills.items(), key=lambda kvp: (-kvp[1], kvp[0]))}
player_pool_sorted = {player: {position: skill for position, skill in sorted(position_skill.items(), key=lambda kvp: (-kvp[1], kvp[0]))} for player, position_skill in player_pool.items()}

for name, skill in players_skills_sorted.items():
    print(f"{name}: {skill} skill")
    for post, skll in player_pool_sorted[name].items():
        print(f"- {post} <::> {skll}")
