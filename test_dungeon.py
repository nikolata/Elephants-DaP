import unittest
from dungeon import Dungeon
from hero import Hero


class TestDungeon(unittest.TestCase):
    def test_spawning_on_first_S(self):
        map = Dungeon("level1.txt", "treasures_file.json")
        hero = Hero(name="Panda", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

        map.spawn(hero)

        self.assertEqual(6, hero.x)
        self.assertEqual(0, hero.y)

    def test_respawning(self):
        map = Dungeon("level1.txt", "treasures_file.json")
        hero = Hero(name="Panda", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

        map.spawn(hero)
        map.spawn(hero)

        self.assertEqual(4, hero.x)
        self.assertEqual(1, hero.y)

    def test_move_hero_in_all_directions(self):
        map = Dungeon("level1.txt", "treasures_file.json")
        hero = Hero(name="Panda", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        map.spawn(hero)
        map.spawn(hero)
        y = hero.y

        map.move_hero("up")
        self.assertEqual(y - 1, hero.y)
        y = hero.y

        map.move_hero("down")
        self.assertEqual(y + 1, hero.y)
        x = hero.x

        map.move_hero("right")
        self.assertEqual(x + 1, hero.x)
        x = hero.x

        map.move_hero("left")

        self.assertEqual(x - 1, hero.x)

    def test_move_hero_to_obstacle_or_outside_the_map_returns_false(self):
        map = Dungeon("level1.txt", "treasures_file.json")
        hero = Hero(name="Panda", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        map.spawn(hero)
        map.spawn(hero)
        y = hero.y
        x = hero.x

        result_with_obstacle = map.move_hero("left")
        self.assertFalse(result_with_obstacle)
        self.assertEqual(y, hero.y)
        self.assertEqual(x, hero.x)

        map.move_hero("up")
        y = hero.y
        x = hero.x
        result_with_boundary = map.move_hero("up")
        self.assertFalse(result_with_boundary)
        self.assertEqual(y, hero.y)
        self.assertEqual(x, hero.x)

    def test_can_attack_reaches_out_of_border(self):
        map = Dungeon("level2.txt", "treasures_file.json")
        hero = Hero(name="Panda", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        map.spawn(hero)

        self.assertFalse(map.can_attack(0, -1, 2))

    def test_can_attack_reaches_obstacle(self):
        map = Dungeon("level2.txt", "treasures_file.json")
        hero = Hero(name="Panda", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        map.spawn(hero)

        self.assertFalse(map.can_attack(0, 1, 3))

    def test_can_attack_finds_enemy(self):
        map = Dungeon("level2.txt", "treasures_file.json")
        hero = Hero(name="Panda", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        map.spawn(hero)

        self.assertEqual((2, 0), map.can_attack(1, 0, 2))

    def test_pick_up_treasure_picks_one_treasure(self):
        map = Dungeon("level1.txt", "treasures_file.json")
        hero = Hero(name="Panda", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        map.spawn(hero)

        map.pick_up_treasure()
        treasures = [hero.spell is not None, 
                    hero.weapon is not None, 
                    hero._healing_potions == 1,
                    hero._mana_potions == 1]

        self.assertTrue(any(treasures))
if __name__ == '__main__':
    unittest.main()
