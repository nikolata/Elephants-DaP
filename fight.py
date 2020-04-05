from weapon import Weapon
from fight_strings import *
from termcolor import colored


class Fight:

    def __init__(self, enemy):
        # loaded = safe_enemys_to_file()       enemys = json.loads(loaded)
        # curr_enemy = enemys['enemy ' + str(enemy_number)]
        # self.enemy = Enemy(curr_enemy['_max_health'], curr_enemy['_max_mana'], curr_enemy['damage'])
        self.enemy = enemy

    def fight(self, hero, first_attack):
        raise ValueError("pop")
        first_round = True
        is_hero_turn = False
        while hero.health != 0 and self.enemy.health != 0:
            if first_round:
                fight_start(hero, self.enemy)
                if isinstance(first_attack, Weapon):
                    print_hero_hits(hero)
                    self.enemy.take_damage(hero.attack(by='weapon'))
                    print_stats(hero, self.enemy)
                else:
                    print_hero_casts(hero)
                    self.enemy.take_damage(hero.attack(by='magic'))
                first_round = False
            else:
                if is_hero_turn is True:
                    print(colored("{}'s turn", 'blue', attrs=['bold']).format(hero.name))
                    print('Choose your next move: ')
                    display_hero_options()
                    move = input().lower()
                    status, error = self.hero_move(hero, move)
                    if status is False:
                        while status is False:
                            status, error = self.handle_errors(hero, error)
                        print_stats(hero, self.enemy)
                        hero.take_mana(None)
                        is_hero_turn = False
                    else:
                        hero.take_mana(None)
                        print_stats(hero, self.enemy)
                        is_hero_turn = False
                else:
                    print(colored("Enemy's turn", 'blue', attrs=['bold']))
                    self.enemy_move(hero)
                    print_stats(hero, self.enemy)
                    is_hero_turn = True
        if self.enemy.is_alive():
            return True
        else:
            return False

    def enemy_move(self, hero):
        if self.enemy._weapon is None:
            weap_dmg = 0
        else:
            weap_dmg = self.enemy._weapon.damage
        if self.enemy._spell is None:
            spell_dmg = 0
        else:
            if self.enemy.mana >= self.enemy._spell._mana_cost:
                spell_dmg = self.enemy._spell.damage
            else:
                spell_dmg = 0
        if weap_dmg > spell_dmg or self.enemy.damage > spell_dmg:
            if self.enemy.y == hero.y and abs(self.enemy.x - hero.x) == 1:
                if weap_dmg > self.enemy.damage:
                    hero.take_damage(self.enemy.attack(by='weapon'))
                    print_enemy_hits(self.enemy, by='weapon')
                else:
                    hero.take_damage(self.enemy.attack())
                    print_enemy_hits(self.enemy, by=None)
            elif abs(self.enemy.y - hero.y) == 1 and self.enemy.x == hero.x:
                if weap_dmg > self.enemy.damage:
                    hero.take_damage(self.enemy.attack(by='weapon'))
                    print_enemy_hits(self.enemy, by='weapon')
                else:
                    hero.take_damage(self.enemy.attack())
                    print_enemy_hits(self.enemy, by=None)
            else:
                self.move_enemy_one_step(hero)
                print('Enemy moves one step closer to Hero. End of enemy turn')
        if spell_dmg > weap_dmg and spell_dmg > self.enemy.damage:
            if abs(hero.x - self.enemy.x) <= self.enemy._spell._cast_range:
                if abs(hero.y - self.enemy.y) <= self.enemy._spell._cast_range:
                    hero.take_damage(self.enemy.attack(by='magic'))
                    print_enemy_casts(self.enemy)
                else:
                    self.move_enemy_one_step(hero)
                    print('Enemy moves one step closer to Hero. End of enemy turn')
            else:
                self.move_enemy_one_step(hero)
                print('Enemy moves one step closer to Hero. End of enemy turn')

    def handle_errors(self, hero, error):
        if error == 'aw':
            print('You dont have a weapon ')
            display_hero_options()
            move = input('Choose something else: ').lower()
            status, error = self.hero_move(hero, move)
        elif error == 'sw':
            print('You dont have a spell ')
            display_hero_options()
            move = input('Choose something else: ').lower()
            status, error = self.hero_move(hero, move)
        elif error == 'not enough mana':
            print('Not enough mana to cast a spell')
            display_hero_options()
            move = input('Choose something else: ').lower()
            status, error = self.hero_move(hero, move)
        elif error == 'not in range':
            print('Not in range to attack with weapon')
            decision = input('Do you want to move to enemy? [y/n]').lower()
            if decision == 'y':
                self.move_hero_one_step(hero)
                status = True
                print('{} moves one step to the enemy. End of his turn!'.format(hero.name))
            else:
                display_hero_options()
                move = input('Choose something else: ').lower()
                status, error = self.hero_move(hero, move)
        elif error == 'no health potions':
            print('No health potions')
            display_hero_options()
            move = input().lower()
            status, error = self.hero_move(hero, move)
        elif error == 'no mana potions':
            print('No mana potions')
            display_hero_options()
            move = input().lower()
            status, error = self.hero_move(hero, move)
        elif error == 'other':
            print('Wrong input, try again ')
            display_hero_options()
            move = input().lower()
            status, error = self.hero_move(hero, move)
        return status, error

    def hero_move(self, hero, move):
        if move == 'aw':
            if hero.weapon is not None:
                if self.enemy.y == hero.y and abs(self.enemy.x - hero.x) == 1:
                    self.enemy.take_damage(hero.attack(by='weapon'))
                    print_hero_hits(hero)
                    return True, None
                elif abs(self.enemy.y - hero.y) == 1 and self.enemy.x == hero.x:
                    self.enemy.take_damage(hero.attack(by='weapon'))
                    print_hero_hits(hero)
                    return True, None
                else:
                    return False, 'not in range'
            else:
                return False, 'aw'
        elif move == 'as':
            if hero.spell is not None:
                if hero._current_mana > hero._spell._mana_cost:
                    self.enemy.take_damage(hero.attack(by='magic'))
                    print_hero_casts(hero)
                    return True, None
                else:
                    return False, 'not enough mana'
            else:
                return False, 'as'
        elif move == 'hp':
            if hero._healing_potions == 0:
                return False, 'no health potions'
            else:
                hero.take_healing(50)
                hero._healing_potions -= 1
                print_hero_takes_health_potions(hero)
                return True, None
        elif move == 'mp':
            if hero._mana_potions == 0:
                return False, 'no mana potions'
            else:
                hero.take_mana(50)
                hero._mana_potions -= 1
                print_hero_takes_mana_potions(hero)
                return True, None
        else:
            return False, 'other'

    def move_hero_one_step(self, hero):
        if hero.y == self.enemy.y and hero.x < self.enemy.x:
            hero.x += 1
        elif hero.y == self.enemy.y and hero.x > self.enemy.x:
            hero.x -= 1
        elif hero.y < self.enemy.y and hero.x == self.enemy.x:
            hero.y += 1
        elif hero.y > self.enemy.y and hero.x == self.enemy.x:
            hero.y -= 1

    def move_enemy_one_step(self, hero):
        if hero.y == self.enemy.y and hero.x < self.enemy.x:
            self.enemy.x -= 1
        elif hero.y == self.enemy.y and hero.x > self.enemy.x:
            self.enemy.x += 1
        elif hero.y < self.enemy.y and hero.x == self.enemy.x:
            self.enemy.y -= 1
        elif hero.y > self.enemy.y and hero.x == self.enemy.x:
            self.enemy.y += 1


'''
s = Spell(name='vqtur', damage=20, mana_cost=40, cast_range=2)
w = Weapon(name='Tupalka', damage=40)
enemy = Enemy(health=100, mana=50, damage=30)
enemy.x = 3
enemy.y = 4
s2 = Spell('vqtur', 50, 15, 2)
w2 = Weapon('Nojka', damage=20)
enemy.learn(s2)
enemy.equip(w2)
f = Fight(enemy)
w = Weapon('kinjal', 30)
h1 = Hero('ivan', 'gorskiq', 180, 50, 5)
h1.x = 3
h1.y = 3
s = Spell('ogin', 60, 20, 3)
h1.learn(s)
h1.equip(w)
f.fight(h1, w)
'''
