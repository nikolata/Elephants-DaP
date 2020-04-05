
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
    'print_hero_takes_health_potions']


def fight_start(hero, enemy):
    FIRST_HALF = 'A fight is started between {} (health={}, mana = {})'.format(hero.name, hero.health, hero.mana)
    SECOND_HALF = 'and Enemy(health={}, mana={}, damage={})'.format(enemy.health, enemy.mana, enemy.damage)
    print(FIRST_HALF, SECOND_HALF)


def print_hero_hits(hero):
    HERO_HITS = '{} hits with {} for {} dmg'.format(hero.name, hero._weapon.name, hero._weapon.damage)
    print(HERO_HITS)


def print_hero_casts(hero):
    HERO_CASTS = '{} casts a {}, hits enemy for {} dmg'.format(hero.name, hero._spell.name, hero._spell.damage)
    print(HERO_CASTS)


def print_enemy_hits(enemy, by):
    if by == 'weapon':
        ENEMY_HITS = 'Enemy hits with {} for {} dmg'.format(enemy._weapon.name, enemy._weapon.damage)
    else:
        ENEMY_HITS = 'Enemy hits with basic atack for {} dmg'.format(enemy.damage)
    print(ENEMY_HITS)


def print_enemy_casts(enemy):
    ENEMY_CASTS = 'Enemy casts a {}, hits enemy for {} dmg'.format(enemy._spell.name, enemy._spell.damage)
    print(ENEMY_CASTS)


def print_hero_information(hero):
    print('{} stats:'.format(hero.name))
    if hero._weapon is None:
        hero_weap = None
    else:
        hero_weap = hero._weapon.damage
    if hero._spell is None:
        hero_spel = None
    else:
        hero_spel = hero._spell.damage
    HERO_INF = "Health:{} Mana:{} Weapon damage:{} Spell damage:{}".format(hero.health, hero.mana, hero_weap, hero_spel)
    HERO_INF2 = 'Health potions: {} Mana potions: {}'.format(hero._health_potions, hero._mana_potions)
    print(HERO_INF, HERO_INF2)


def print_enemy_information(enemy):
    print('Enemy stats:')
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
    print(ENEMY_INF_1, ENEMY_INF_2)


def print_hero_takes_health_potions(hero):
    print('{} drank health potion. End of turn.').format(hero.name)


def print_hero_takes_mana_potions(hero):
    print('{} drank mana potion. End of turn.').format(hero.name)


def print_stats(hero, enemy):
    print_hero_information(hero)
    print_enemy_information(enemy)


def display_hero_options():
    OPTIONS = 'AW = Atack with weapon/ AS = Atack with spell/ HP = Use Health Potion/ MP = Use Mana Potion'
    print(OPTIONS)
