from classes.character import Character
from classes.magic import player_spells, enemy_spells
from classes.backpack import player_items
from classes.bcolors import bcolors
from random import randrange


# Creating characters
player1 = Character('Bezimienny', 2950, 135, 185, 55, player_spells, player_items)
player2 = Character('Diego     ', 1400, 30, 140, 40, player_spells, player_items)
player3 = Character('Milten    ', 1250, 300, 45, 25, player_spells, player_items)

enemy1 = Character('Priest ', 1500, 200, 20, 30, enemy_spells, [])
enemy2 = Character('Śniący ', 6000, 110, 600, 80, enemy_spells, [])
enemy3 = Character('Warrior', 1500, 0, 300, 50, enemy_spells, [])

players = [player1, player2, player3]
dead_players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]
dead_enemies = [enemy1, enemy2, enemy3]

# Let's play

play = True
print(bcolors.MBOLD + bcolors.MYELLOW + '|' + '-'*52 + '|' + bcolors.ENDC)
print(bcolors.MBOLD + bcolors.MYELLOW + '|' + '='*8 + 'You finally found Arch-Demon Sleeper' + '='*8 + '|' + bcolors.ENDC)
print(bcolors.MBOLD + bcolors.MYELLOW + '|' + '='*8 + 'You must defeat him to save Khorinis' + '='*8 + '|' + bcolors.ENDC)
print(bcolors.MBOLD + bcolors.MYELLOW + '|' + '-'*52 + '|' + bcolors.ENDC)
while play:
    print(bcolors.MBLACKBG + '='*80 + bcolors.ENDC)
    print(bcolors.MBOLD + 'NAME               HP                                     MP' + bcolors.ENDC)
    for player in players:
        player.get_stats()
    print('\n')
    for enemy in enemies:
        enemy.get_enemy_stats()

    print(bcolors.MBOLD + bcolors.MVIOLET + '\n=========PLAYER TURN========' + bcolors.ENDC)

    for player in players:
        player.choose_action()
        choice = int(input(' Choose action: ')) - 1
        current_mp = player.get_mp()

        if choice == 0:                                             # Normal Attack
            dmg = player.generate_dmg()
            target = player.choose_target(enemies)
            enemies[target].take_dmg(dmg)
            print(bcolors.MRED + "\n" + player.name.replace(' ', '') + " attacked " +
                  enemies[target].name.replace(" ", "") + " for", dmg, "points of damage." + bcolors.ENDC)

            if enemies[target].get_hp() == 0:
                print(bcolors.MRED + bcolors.MBOLD + enemies[target].name.replace(' ', '') + ' has died.' + bcolors.ENDC)
                del enemies[target]
                if len(enemies) == 0:
                    break

        elif choice == 1:                                           # Use magic
            magic = player.choose_magic()

            if magic == -1:
                continue

            spell = player_spells[magic]
            dmg = spell.generate_dmg()

            if spell.cost > current_mp:
                print(bcolors.MRED + '\nYou don\'t have enough magic points' + bcolors.ENDC)
                continue

            if spell.typ == 'dmg':
                target = player.choose_target(enemies)
                enemies[target].take_dmg(dmg)
                player.reduce_mp(spell.cost)
                print(bcolors.MBLUE + '\nYou attack ' + enemies[target].name.replace(' ', '') +
                      ' for: {} dmg using spell {}.'.format(dmg, spell.name) + bcolors.ENDC)
                if enemies[target].get_hp() == 0:
                    print(enemies[target].name.replace(' ', '') + ' has died.')
                    del enemies[target]
                    if len(enemies) == 0:
                        break

            else:
                target = player.choose_target(players)
                players[target].heal(dmg)
                player.reduce_mp(spell.cost)
                print(bcolors.MBLUE + '\nYou heal {} for: {} using spell {}.'
                      .format(players[target].name.replace(" ", ""), dmg, spell.name) + bcolors.ENDC)

        elif choice == 2:                                                   # Use item
            backpack = player.choose_item()
            item = player.items[backpack]

            if backpack == -1:
                continue

            if item['quantity'] < 0:
                print('You already used all {}'.format(item['item'].name))
                continue

            item['quantity'] -= 1

            if item['item'].typ == 'attack':
                dmg = item['item'].prop
                target = player.choose_target(enemies)
                enemies[target].take_dmg(dmg)
                print(bcolors.MGREEN2 + '\nYou attack ' + enemies[target].name.replace(' ', '') +
                      ' using {} for: {} dmg'.format(item['item'].name, item['item'].prop) + bcolors.ENDC)
                if enemies[target].get_hp() == 0:
                    print(enemies[target].name.replace(' ', '') + ' has died.')
                    del enemies[target]
                    if len(enemies) == 0:
                        break

            elif item['item'].typ == 'potion':
                player.heal(item['item'].prop)
                print(bcolors.MGREEN + '\n' + item['item'].name + ' heals you for:', str(item['item'].prop), 'HP'
                      + bcolors.ENDC)

            else:
                if item['item'].name == 'MegaElixer':
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp

                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolors.MGREEN + '\n' + item['item'].name + ' full restores HP & MP' + bcolors.ENDC)

# checking if there are still enemies
    defeated_enemies = 0
    for enem in dead_enemies:
        if enem.get_hp() == 0:
            defeated_enemies += 1
        if defeated_enemies == 3:
            print(bcolors.MGREEN + bcolors.MBOLD + '\nYou win! Korinis is safe!' + bcolors.ENDC)
            play = False

    print(bcolors.MBOLD + bcolors.MVIOLET + '\n=========ENEMY TURN========\n' + bcolors.ENDC)

    for enemy in enemies:
        action = randrange(0, 2)

        if action == 0 or enemy.mp < 25:                                    # Normal attack
            target = randrange(0, len(players))
            dmg = enemy.generate_dmg()
            players[target].take_dmg(dmg)
            print(bcolors.MBOLD + bcolors.MRED + enemy.name.replace(" ", "") + " attacks " +
                  players[target].name.replace(" ", "") + " for", str(dmg) + bcolors.ENDC)

            if players[target].get_hp() == 0:
                print(players[target].name.replace(" ", "") + " has died.")
                del players[target]
                if len(players) == 0:
                    break

        elif action == 1:                                                   # Use magic
            allow = False
            while not allow:
                tmp = randrange(0, len(enemy.magic))
                spell = enemy.magic[tmp]
                pct = enemy.hp / enemy.maxhp * 100
                if enemy.mp < spell.cost or (spell.typ == "heal" and pct > 50):
                    continue
                else:
                    allow = True

            enemy.reduce_mp(spell.cost)
            magic_dmg = spell.generate_dmg()

            if spell.typ == "heal":
                enemy.heal(magic_dmg)
                print(bcolors.MBOLD + bcolors.MBLUE + spell.name + " heals " + enemy.name.replace(' ', '') +
                      " for", str(magic_dmg), "HP." + bcolors.ENDC)

            elif spell.typ == "dmg":

                target = randrange(0, len(players))

                players[target].take_dmg(magic_dmg)

                print(bcolors.MBOLD + bcolors.MBLUE + enemy.name.replace(" ", "") + "'s " + spell.name + " deals",
                      str(magic_dmg), "points of damage to " + players[target].name.replace(" ", "") + bcolors.ENDC)

                if players[target].get_hp() == 0:
                    print(players[target].name.replace(" ", "") + " has died.")
                    del players[target]
                    if len(players) == 0:
                        break

    print('\n')
# checking if there are still any players
    defeated_players = 0
    for player in dead_players:
        if player.get_hp() == 0:
            defeated_players += 1
        if defeated_players == 3:
            print(bcolors.MBOLD + bcolors.MRED + '\nYou lost and everything is lost! There is no more hope...'
                  + bcolors.ENDC)
            play = False
