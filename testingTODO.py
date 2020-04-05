from dungeon import Dungeon
from hero import Hero

map = Dungeon("level1.txt", "treasures_file.json", "enemies.json")
hero = Hero(name="Panda", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
map.spawn(hero)


def stats():
    print("Weapon: " + str(hero._weapon))
    print("HPotions: " + str(hero._healing_potions))
    print("Spell: " + str(hero._spell))
    print("MPotions: " + str(hero._mana_potions))

map.move_hero("right")
map.move_hero("right")
map.move_hero("right")

for i in range(10):
    map.pick_up_treasure()