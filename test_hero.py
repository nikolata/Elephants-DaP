import unittest
from hero import Hero
from spell import Spell


class TestHero(unittest.TestCase):
    def test_take_mana_when_making_a_move(self):
        # hero = Hero(name="Panda", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        # spell = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        # hero.learn(spell)
        # hero.attack(by="magic")

        # hero.take_mana(None)

        # self.assertEqual(52, hero.mana)
        pass


if __name__ == '__main__':
    unittest.main()
