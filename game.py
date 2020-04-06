from dungeon import Dungeon
from hero import Hero
from weapon import Weapon
from spell import Spell
from termcolor import colored


def stats(hero):
    print('Health: ' + str(hero.health))
    print('Mana: ' + str(hero.mana))
    print("Weapon: " + str(hero._weapon))
    print("Spell: " + str(hero._spell))
    print("HPotions: " + str(hero._healing_potions))
    print("MPotions: " + str(hero._mana_potions))


def commands():
    print(colored('To move aroung use up/left/right/down', 'cyan', attrs=['bold']))
    print(colored('To see your stats use "stats"', 'cyan', attrs=['bold']))
    print(colored('To attack use "attack"', 'cyan', attrs=['bold']))
    print(colored('To see the map use "map"', 'cyan', attrs=['bold']))


def game_cycle_level(battle_map, hero):
    has_game_ended = False
    while has_game_ended is False:
        move = input('What is your move: ').lower()

        if move == 'up' or move == 'left' or move == 'right' or move == 'down':
            battle_map.move_hero(move)
        elif move == 'stats':
            stats(hero)
        elif move == 'attack':
            type_att = input('To choose attack use weapon/magic: ')
            battle_map.hero_attack(by=type_att)
        elif move == 'map':
            battle_map.print_map()
        elif move == 'help':
            commands()
        else:
            print('No such option. Try again.')

        has_game_ended = battle_map.can_exit()
        if hero.health == 0:
            break


def play_game():
    battle_map = Dungeon(map_file="level1.txt", treasure_file="treasures_file.json", enemy_file="enemies.json")
    hero_name = input('ENTER YOUR BATTLE NAME: ')
    hero_title = input('ENTER YOUR TITLE: ')
    hero = Hero(name=hero_name, title=hero_title, health=100, mana=50, mana_regeneration_rate=5)
    name = hero.known_as()
    print('Welcome {} to level1. Wish you luck, you will need it!'.format(name))
    start_weapon = Weapon(name='Pruchka', damage=25)
    start_spell = Spell(name='Vqtur', damage=30, mana_cost=35, cast_range=2)
    hero.equip(start_weapon)
    hero.learn(start_spell)
    battle_map.spawn(hero)
    battle_map.print_map()
    print(colored('TUTORIAL', 'cyan', attrs=['bold']))
    commands()
    print(colored('To see the commands use "help"', 'cyan', attrs=['bold']))
    game_cycle_level(battle_map, hero)

    if hero.is_alive() is False:
        return 0
    start_level2 = input('Do you want to play on level2? [y/n] ').lower()

    if start_level2[0] == 'y':
        battle_map = Dungeon(map_file="level2.txt", treasure_file="treasures_file.json", enemy_file="enemies.json")
        battle_map.spawn(hero)
        battle_map.print_map()
        game_cycle_level(battle_map, hero)
        print('GOOD JOB! YOU BEAT THE WHOLE GAME!')
    else:
        print('Ha,ha,ha. You are a coward')
