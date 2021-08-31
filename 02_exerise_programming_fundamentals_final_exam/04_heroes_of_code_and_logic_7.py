number_of_heroes = int(input())

heroes_dict = {}

for i in range(number_of_heroes):
    heroe = input().split()
    hero_name = heroe[0]
    hit_points = int(heroe[1])
    mana_points = int(heroe[2])
    heroes_dict[hero_name] = {'hit points': hit_points, 'mana points': mana_points}

command = input()

while command != "End":

    if "CastSpell" in command:
        cmd = command.split(' - ')
        name = cmd[1]
        mp_needed = int(cmd[2])
        spell_name = cmd[3]

        if mp_needed <= heroes_dict[name]['mana points']:
            heroes_dict[name]['mana points'] -= mp_needed
            print(f"{name} has successfully cast {spell_name} and now has {heroes_dict[name]['mana points']} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")

    elif "TakeDamage" in command:
        cmd = command.split(' - ')
        name = cmd[1]
        damage = int(cmd[2])
        attacker = cmd[3]
        heroes_dict[name]['hit points'] -= damage

        if heroes_dict[name]['hit points'] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes_dict[name]['hit points']} HP left!")
        else:
            del heroes_dict[name]
            print(f"{name} has been killed by {attacker}!")

    elif "Recharge" in command:
        cmd = command.split(' - ')
        name = cmd[1]
        amount = int(cmd[2])
        current_mana_shortage = 200 - heroes_dict[name]['mana points']
        if amount > current_mana_shortage:
            heroes_dict[name]['mana points'] = 200
            print(f"{name} recharged for {current_mana_shortage} MP!")
        else:
            heroes_dict[name]['mana points'] += amount
            print(f"{name} recharged for {amount} MP!")

    elif "Heal" in command:
        cmd = command.split(' - ')
        name = cmd[1]
        amount = int(cmd[2])
        current_hp_shortage = 100 - heroes_dict[name]['hit points']
        if amount > current_hp_shortage:
            heroes_dict[name]['hit points'] = 100
            print(f"{name} healed for {current_hp_shortage} HP!")
        else:
            heroes_dict[name]['hit points'] += amount
            print(f"{name} healed for {amount} HP!")

    command = input()


sorted_heroes_dict = sorted(heroes_dict.items(), key=lambda x: (-x[1]['hit points'], x[0]))

for key, val in sorted_heroes_dict:
    print(f"{key}")
    print(f"  HP: {val['hit points']}")
    print(f"  MP: {val['mana points']}")
