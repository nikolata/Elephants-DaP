import unittest
from fight import Fight
from hero import Hero
from enemy import Enemy
from weapon import Weapon
from spell import Spell


class TestFight(unittest.TestCase):

    def test_hero_move_with_aw_and_equiped_weapon_should_return_true(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        w = Weapon('nojka', 25)
        h.equip(w)
        h.x = 2
        h.y = 3
        fight = Fight(enemy_number=3, enemy_x=3, enemy_y=3)
        status, error = fight.hero_move(h, 'aw')
        self.assertTrue(status)

    def test_hero_move_with_aw_and_equiped_weapon_and_not_in_range_should_return_false_and_not_in_range(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        w = Weapon('nojka', 25)
        h.equip(w)
        h.x = 1
        h.y = 3
        fight = Fight(enemy_number=3, enemy_x=3, enemy_y=3)
        status, error = fight.hero_move(h, 'aw')
        self.assertFalse(status)
        self.assertEqual(error, 'not in range')

    def test_hero_move_with_aw_and_not_equiped_weapon_should_return_false(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        fight = Fight(enemy_number=3, enemy_x=3, enemy_y=3)
        status, error = fight.hero_move(h, 'aw')
        self.assertFalse(status)
        self.assertEqual(error, 'aw')

    def test_hero_move_with_as_and_learned_spell_should_return_true(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        s = Spell('fireball', 25, 15, 3)
        h.learn(s)
        fight = Fight(enemy_number=3, enemy_x=3, enemy_y=3)
        status = fight.hero_move(h, 'as')
        self.assertTrue(status)

    def test_hero_move_with_as_and_not_learned_spell_should_return_false(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        fight = Fight(enemy_number=3, enemy_x=3, enemy_y=3)
        status, error = fight.hero_move(h, 'as')
        self.assertFalse(status)
        self.assertEqual(error, 'as')

    def test_if_hero_move_input_is_not_from_our_options_should_return_false_and_other(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        fight = Fight(enemy_number=3, enemy_x=3, enemy_y=3)
        status, error = fight.hero_move(h, 'test')
        self.assertFalse(status)
        self.assertEqual(error, 'other')

    def test_if_move_hero_one_step_moves_hero_x_with_one_position_on_right(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        fight = Fight(enemy_number=3, enemy_x=3, enemy_y=3)
        h.x = 1
        h.y = 3
        fight.move_hero_one_step(h)
        self.assertEqual(h.x, 2)

    def test_if_move_hero_one_step_moves_hero_x_with_one_position_on_left(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        fight = Fight(enemy_number=3, enemy_x=3, enemy_y=3)
        h.x = 5
        h.y = 3
        fight.move_hero_one_step(h)
        self.assertEqual(h.x, 4)

    def test_if_move_hero_one_step_moves_hero_y_with_one_position_down(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        fight = Fight(enemy_number=3, enemy_x=3, enemy_y=3)
        h.x = 3
        h.y = 1
        fight.move_hero_one_step(h)
        self.assertEqual(h.y, 2)

    def test_if_move_hero_one_step_moves_hero_y_with_one_position_up(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        fight = Fight(enemy_number=3, enemy_x=3, enemy_y=3)
        h.x = 3
        h.y = 5
        fight.move_hero_one_step(h)
        self.assertEqual(h.y, 4)


if __name__ == '__main__':
    unittest.main()
