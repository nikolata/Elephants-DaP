from enemy import Enemy
import json
from enemys_to_json import safe_enemys_to_file
from hero import Hero
from weapon import Weapon

class Fight:

    def __init__(self, enemy_number):
        loaded = safe_enemys_to_file()
        enemys = json.loads(loaded)
        curr_enemy = enemys['enemy ' + str(enemy_number)]
        self.enemy = Enemy(curr_enemy['_max_health'], curr_enemy['_max_mana'], curr_enemy['damage'])

    def fight(self, hero, first_attack):
        first_round = True
        while hero.health != 0 and self.enemy.health != 0:
            if first_round:
                print('A fight is started between {} (health={}, mana={})'
                    ' and Enemy(health={}, mana={}, damage={})'\
                    .format(hero.name, hero.health, hero.mana, self.enemy.health, self.enemy.mana, self.enemy.damage))
                if isinstance(first_attack, Weapon):
                    self.print_hero_hits(hero)

            break

    def print_hero_hits(self, hero):
        print('{} hits with {} for {}').format(hero.name, hero._weapon.name, hero._weapon.damage)

    def print_enemy_hits(self):
        print('{} hits with {} for {}').format(self.enemy.name, self.enemy._weapon.name, self.enemy._weapon.damage)

    def print_hero_information(self, hero):
        print("Health:{} Mana:{} Weapon damage:{} Spell damage:{}").format(hero.health, hero.mana, hero._weapon.damage)


f = Fight(2)
h1 = Hero('ivan', 'gorskiq', 100, 50, 5)
f.fight(h1, 'magic')
