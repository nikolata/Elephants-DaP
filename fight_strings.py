from termcolor import colored

__all__ = [
    'fight_start',
    'print_hero_hits',
    'print_hero_casts',
    'print_enemy_hits',
    'print_enemy_casts',
    'print_hero_information',
    'print_enemy_information',
    'print_stats',
    'display_hero_options',
    'print_hero_takes_health_potions',
    'print_hero_takes_mana_potions']


def fight_start(hero, enemy):
    FIRST_HALF = 'A fight is started between {} (health={}, mana = {})'.format(hero.name, hero.health, hero.mana)
    SECOND_HALF = 'and Enemy(health={}, mana={}, damage={})'.format(enemy.health, enemy.mana, enemy.damage)
    print(colored(FIRST_HALF, 'cyan', attrs=['bold']), colored(SECOND_HALF, 'cyan', attrs=['bold']))


def print_hero_hits(hero):
    HERO_HITS = '{} hits with {} for {} dmg'.format(hero.name, hero._weapon.name, hero._weapon.damage)
    print(colored(HERO_HITS, 'red'))


def print_hero_casts(hero):
    HERO_CASTS = '{} casts a {}, hits enemy for {} dmg'.format(hero.name, hero._spell.name, hero._spell.damage)
    print(colored(HERO_CASTS, 'red'))


def print_enemy_hits(enemy, by):
    if by == 'weapon':
        ENEMY_HITS = 'Enemy hits with {} for {} dmg'.format(enemy._weapon.name, enemy._weapon.damage)
    else:
        ENEMY_HITS = 'Enemy hits with basic atack for {} dmg'.format(enemy.damage)
    print(colored(ENEMY_HITS, 'yellow'))


def print_enemy_casts(enemy):
    ENEMY_CASTS = 'Enemy casts a {}, hits enemy for {} dmg'.format(enemy._spell.name, enemy._spell.damage)
    print(colored(ENEMY_CASTS, 'yellow'))


def print_hero_information(hero):
    print(colored('{} stats:', 'green').format(hero.name))
    if hero._weapon is None:
        hero_weap = None
    else:
        hero_weap = hero._weapon.damage
    if hero._spell is None:
        hero_spel = None
    else:
        hero_spel = hero._spell.damage
    HERO_INF = "Health:{} Mana:{} Weapon damage:{} Spell damage:{}".format(hero.health, hero.mana, hero_weap, hero_spel)
    HERO_INF2 = 'Health potions: {} Mana potions: {}'.format(hero._healing_potions, hero._mana_potions)
    print(colored(HERO_INF, 'cyan'), colored(HERO_INF2, 'cyan'))


def print_enemy_information(enemy):
    print(colored('Enemy stats:', 'green'))
    if enemy._weapon is None:
        enemy_weap = None
    else:
        enemy_weap = enemy._weapon.damage
    if enemy._spell is None:
        enemy_spel = None
    else:
        enemy_spel = enemy._spell.damage
    ENEMY_INF_1 = "Health:{} Mana:{} Weapon damage:{}".format(enemy.health, enemy.mana, enemy_weap)
    ENEMY_INF_2 = "Spell damage:{} Basic damage: {}".format(enemy_spel, enemy.damage)
    print(colored(ENEMY_INF_1, 'cyan'), colored(ENEMY_INF_2, 'cyan'))


def print_hero_takes_health_potions(hero):
    print(colored('{} drank health potion. End of turn.', 'blue').format(hero.name))


def print_hero_takes_mana_potions(hero):
    print(colored('{} drank mana potion. End of turn.', 'blue').format(hero.name))


def print_stats(hero, enemy):
    print_hero_information(hero)
    print_enemy_information(enemy)


def display_hero_options():
    OPTIONS = 'AW = Atack with weapon/ AS = Atack with spell/ HP = Use Health Potion/ MP = Use Mana Potion'
    print(colored(OPTIONS, 'cyan'))
