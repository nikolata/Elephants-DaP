import unittest
from hero import Hero
from spell import Spell
from dungeon import Dungeon


class TestHero(unittest.TestCase):
    def test_take_mana_when_making_a_move(self):
        map = Dungeon("level1.txt", "treasures_file.json")
        hero = Hero(name="Panda", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        map.spawn(hero)

        hero._current_mana = 50
        map.move_hero("left")

        self.assertEqual(52, hero.mana)

    def test_take_mana_when_given_potion(self):
        hero = Hero(name="Panda", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

        hero._current_mana = 50
        hero.take_mana(50)

        self.assertEqual(100, hero.mana)

if __name__ == '__main__':
    unittest.main()
