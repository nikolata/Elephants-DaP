from random import choice
from treasure import Treasure
import json
from spell import Spell
from weapon import Weapon


class Dungeon:
    spawning_point = 'S'
    gateway = 'G'
    treasure = 'T'
    obstacle = '#'
    path = '.'
    enemy = 'E'
    hero_symbol = 'H'

    def __init__(self, map_file, treasure_file):
        with open(map_file, 'r') as f:
            self.map = f.readlines()
            self.map = [list(x[:-1]) for x in self.map]
            self.hero = None
        with open(treasure_file, 'r') as f2:
            treasure_dictionary = json.load(f2)
            self.weapons = treasure_dictionary["weapons"]
            self.spells = treasure_dictionary["spells"]

    def print_map(self):
        if self.hero is not None:
            if self.hero.x is not None and self.hero.y is not None:
                previous_symbol = self.map[self.hero.y][self.hero.x]
                self.map[self.hero.y][self.hero.x] = self.hero_symbol
                for x in self.map:
                    print("".join(x))
                self.map[self.hero.y][self.hero.x] = previous_symbol
        else:
            for x in self.map:
                print("".join(x))

    def spawn(self, hero):
        self.hero = hero
        for y in range(len(self.map)):
            if self.spawning_point in self.map[y]:
                x = self.map[y].index(self.spawning_point)
                self.hero.x = x
                self.hero.y = y
                self.map[self.hero.y][self.hero.x] = self.path
                break

    def pick_up_treasure(self):
        treasure = choice(list(Treasure))
        if treasure == Treasure.Weapon:
            weapon = choice(self.weapons)
            weapon = Weapon(weapon["name"], weapon["damage"])
            self.hero.equip(weapon)
        if treasure == Treasure.Spell:
            spell = choice(self.spells)
            spell = Spell(spell["name"], spell["damage"], spell["mana_cost"], spell["cast_range"])
            self.hero.learn(spell)
        if treasure == Treasure.Health:
            self.hero.receive_health_potion()
        if treasure == Treasure.Mana:
            self.hero.receive_mana_potion()

    def move_hero(self, direction):
        y = self.hero.y
        x = self.hero.x
        if direction == "up":
            self.hero.y -= 1
        elif direction == "down":
            self.hero.y += 1
        elif direction == "right":
            self.hero.x += 1
        elif direction == "left":
            self.hero.x -= 1

        if not 0 <= self.hero.x < len(self.map[0]):
            self.hero.x = x
            return False

        if not 0 <= self.hero.y < len(self.map):
            self.hero.y = y
            return False

        if self.map[self.hero.y][self.hero.x] == self.obstacle:
            self.hero.x = x
            self.hero.y = y
            return False

        if self.map[self.hero.y][self.hero.x] == self.treasure:
            self.pick_up_treasure()
            self.map[self.hero.y][self.hero.x] = self.path

        if self.map[self.hero.y][self.hero.x] == self.enemy:
            # self.start_a_fight()
            self.map[self.hero.y][self.hero.x] = self.path

        return True

    def can_attack(self, y, x, attack_range):
        for k in range(1, attack_range + 1):
            if not 0 <= self.hero.x + x * k < len(self.map[0]) or not 0 <= self.hero.y < len(self.map):
                return False
            if self.map[self.hero.y + y * k][self.hero.x + x * k] == self.obstacle:
                return False
            if self.map[self.hero.y + y * k][self.hero.x + x * k] == self.enemy:
                return (self.hero.y + y * k, self.hero.x + x * k)
        return False

    def try_attack(self, attack_range):
        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]
        for i in range(4):
            attack = self.can_attack(y[i], x[i], attack_range)
            if attack:
                if self.start_a_fight():
                    self.map[attack[0]][attack[1]] = self.path
                break

    def hero_attack(self, by):
        if by == "weapon":
            self.try_attack(1)
        if by == "magic":
            try:
                if self.hero.can_cast():
                    cast_range = self.hero.spell.cast_range
                    self.try_attack(cast_range)
            except Exception as err:
                print(err)
