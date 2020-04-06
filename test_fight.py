import unittest
from fight import Fight
from hero import Hero
from enemy import Enemy
from weapon import Weapon
from spell import Spell


class TestHeroMove(unittest.TestCase):

    def test_hero_move_with_aw_and_equiped_weapon_should_return_true(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        w = Weapon('nojka', 25)
        h.equip(w)
        h.x = 2
        h.y = 3
        enemy = Enemy(health=100, mana=40, damage=60)
        enemy.x = 3
        enemy.y = 3
        fight = Fight(enemy)
        status, error = fight.hero_move(h, 'aw')
        self.assertTrue(status)

    def test_hero_move_with_aw_and_equiped_weapon_and_not_in_range_should_return_false_and_not_in_range(self):
        # y level is the same, but abs(enemy.x - hero.x) is not equal to 1
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        w = Weapon('nojka', 25)
        h.equip(w)
        h.x = 1
        h.y = 3
        enemy = Enemy(health=100, mana=40, damage=60)
        enemy.x = 3
        enemy.y = 3
        fight = Fight(enemy)
        status, error = fight.hero_move(h, 'aw')
        self.assertFalse(status)
        self.assertEqual(error, 'not in range')

    def test_hero_move_with_aw_and_equiped_weapon_and_not_in_range_should_return_false_and_not_in_range_2(self):
        # x column is the same, but abs(enemy.y - hero.y) is not equal to 1
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        w = Weapon('nojka', 25)
        h.equip(w)
        h.x = 3
        h.y = 1
        enemy = Enemy(health=100, mana=40, damage=60)
        enemy.x = 3
        enemy.y = 3
        fight = Fight(enemy)
        status, error = fight.hero_move(h, 'aw')
        self.assertFalse(status)
        self.assertEqual(error, 'not in range')

    def test_hero_move_with_aw_and_not_equiped_weapon_should_return_false_and_aw(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=60)
        enemy.x = 3
        enemy.y = 3
        fight = Fight(enemy)
        status, error = fight.hero_move(h, 'aw')
        self.assertFalse(status)
        self.assertEqual(error, 'aw')

    def test_hero_move_with_as_and_learned_spell_should_return_true_and_as(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        s = Spell('fireball', 25, 15, 3)
        h.learn(s)
        enemy = Enemy(health=100, mana=40, damage=60)
        enemy.x = 3
        enemy.y = 3
        fight = Fight(enemy)
        status = fight.hero_move(h, 'as')
        self.assertTrue(status)

    def test_hero_move_with_as_and_not_learned_spell_should_return_false_and_as(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=60)
        enemy.x = 3
        enemy.y = 3
        fight = Fight(enemy)
        status, error = fight.hero_move(h, 'as')
        self.assertFalse(status)
        self.assertEqual(error, 'as')

    def test_hero_move_with_as_and_learned_spell_but_not_enough_mana_should_return_false_and_not_enough_mana(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=50, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=60)
        spell = Spell(name='Test Magiq', damage=40, mana_cost=60, cast_range=1)
        enemy.x = 3
        enemy.y = 3
        h.learn(spell)
        fight = Fight(enemy)
        status, error = fight.hero_move(h, 'as')
        self.assertFalse(status)
        self.assertEqual(error, 'not enough mana')

    def test_if_hero_move_input_is_not_from_our_options_should_return_false_and_other(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=60)
        enemy.x = 3
        enemy.y = 3
        fight = Fight(enemy)
        status, error = fight.hero_move(h, 'test')
        self.assertFalse(status)
        self.assertEqual(error, 'other')


class TestMoveHeroOneStep(unittest.TestCase):
    def test_if_move_hero_one_step_moves_hero_x_with_one_position_on_right(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=60)
        enemy.x = 3
        enemy.y = 3
        fight = Fight(enemy)
        h.x = 1
        h.y = 3
        fight.move_hero_one_step(h)
        self.assertEqual(h.x, 2)

    def test_if_move_hero_one_step_moves_hero_x_with_one_position_on_left(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=60)
        enemy.x = 3
        enemy.y = 3
        fight = Fight(enemy)
        h.x = 5
        h.y = 3
        fight.move_hero_one_step(h)
        self.assertEqual(h.x, 4)

    def test_if_move_hero_one_step_moves_hero_y_with_one_position_down(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=60)
        enemy.x = 3
        enemy.y = 3
        fight = Fight(enemy)
        h.x = 3
        h.y = 1
        fight.move_hero_one_step(h)
        self.assertEqual(h.y, 2)

    def test_if_move_hero_one_step_moves_hero_y_with_one_position_up(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=60)
        enemy.x = 3
        enemy.y = 3
        fight = Fight(enemy)
        h.x = 3
        h.y = 5
        fight.move_hero_one_step(h)
        self.assertEqual(h.y, 4)


class TestEnemyMove(unittest.TestCase):

    def test_enemy_move_with_same_y_level_as_hero_and_x_in_range_to_attack_with_weapon_should_reduce_hero_health(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        weapon = Weapon(name='Pruchka', damage=40)
        enemy = Enemy(health=100, mana=40, damage=20)
        enemy.x = 2
        enemy.y = 3
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(h.health, 60)

    def test_enemy_move_with_same_y_level_as_hero_and_x_in_range_to_attack_with_spell_should_reduce_hero_health(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        s = Spell('fireball', damage=45, mana_cost=15, cast_range=3)
        weapon = Weapon(name='Pruchka', damage=40)
        enemy = Enemy(health=100, mana=40, damage=20)
        enemy.x = 2
        enemy.y = 3
        enemy.learn(s)
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(h.health, 55)

    def test_enemy_move_with_same_y_as_hero_and_x_in_range_to_attack_choose_weapon_not_spell_reduces_hero_health(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        s = Spell('fireball', damage=25, mana_cost=15, cast_range=3)
        weapon = Weapon(name='Pruchka', damage=40)
        enemy = Enemy(health=100, mana=40, damage=20)
        enemy.x = 2
        enemy.y = 3
        enemy.learn(s)
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(h.health, 60)

    def test_enemy_move_with_same_y_as_hero_and_x_in_range_to_attack_choose_spell_not_weapon_reduces_hero_health(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        s = Spell('fireball', damage=45, mana_cost=15, cast_range=3)
        enemy = Enemy(health=100, mana=40, damage=20)
        weapon = Weapon(name='Pruchka', damage=40)
        enemy.x = 2
        enemy.y = 3
        enemy.learn(s)
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(h.health, 55)

    def test_enemy_with_same_y_as_hero_and_x_in_range_to_attack_choose_normal_attack_reduces_hero_health(self):
        # test without spell and weapon
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=60)
        enemy.x = 2
        enemy.y = 3
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(h.health, 40)

    def test_enemy_with_same_y_as_hero_and_x_in_range_to_attack_choose_normal_attack_reduces_hero_health_2(self):
        # test with spell only and enemy dmg > spell dmg
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=60)
        enemy.x = 2
        enemy.y = 3
        s = Spell('fireball', damage=45, mana_cost=15, cast_range=3)
        enemy.learn(s)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(h.health, 40)

    def test_enemy_with_same_y_as_hero_and_x_in_range_to_attack_choose_normal_attack_reduces_hero_health_3(self):
        # test with weapon only and enemy dmg > weapon dmg
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=60)
        enemy.x = 2
        enemy.y = 3
        weapon = Weapon(name='Pruchka', damage=50)
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(h.health, 40)

    def test_enemy_with_same_y_as_hero_and_x_in_range_to_attack_choose_normal_attack_reduces_hero_health_4(self):
        # test with weapon and spell and enemy dmg > weapon dmg > spell dmg
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=60)
        enemy.x = 2
        enemy.y = 3
        weapon = Weapon(name='Pruchka', damage=50)
        s = Spell('fireball', damage=45, mana_cost=15, cast_range=3)
        enemy.learn(s)
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(h.health, 40)

    def test_enemy_with_same_y_as_hero_and_x_in_range_to_attack_choose_normal_attack_reduces_hero_health_5(self):
        # test with weapon and spell and enemy dmg > spell dmg > weapon dmg
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=60)
        enemy.x = 2
        enemy.y = 3
        weapon = Weapon(name='Pruchka', damage=50)
        s = Spell('fireball', damage=45, mana_cost=15, cast_range=3)
        enemy.learn(s)
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(h.health, 40)

    def test_enemy_move_with_same_x_level_as_hero_and_y_in_range_to_attack_with_weapon_should_reduce_hero_health(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        weapon = Weapon(name='Pruchka', damage=40)
        enemy = Enemy(health=100, mana=40, damage=20)
        enemy.x = 3
        enemy.y = 2
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(h.health, 60)

    def test_enemy_move_with_same_x_level_as_hero_and_y_in_range_to_attack_with_spell_should_reduce_hero_health(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        s = Spell('fireball', damage=45, mana_cost=15, cast_range=3)
        enemy = Enemy(health=100, mana=40, damage=20)
        enemy.x = 3
        enemy.y = 2
        enemy.learn(s)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(h.health, 55)

    def test_enemy_move_with_same_x_as_hero_and_y_in_range_to_attack_choose_weapon_not_spell_reduces_hero_health(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        s = Spell('fireball', damage=25, mana_cost=15, cast_range=3)
        weapon = Weapon(name='Pruchka', damage=40)
        enemy = Enemy(health=100, mana=40, damage=20)
        enemy.x = 3
        enemy.y = 2
        enemy.learn(s)
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(h.health, 60)

    def test_enemy_move_with_same_x_as_hero_and_y_in_range_to_attack_choose_spell_not_weapon_reduces_hero_health(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        s = Spell('fireball', damage=55, mana_cost=15, cast_range=3)
        enemy = Enemy(health=100, mana=40, damage=20)
        weapon = Weapon(name='Pruchka', damage=50)
        enemy.x = 3
        enemy.y = 2
        enemy.learn(s)
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(h.health, 45)

    def test_enemy_with_same_x_as_hero_and_y_in_range_to_attack_choose_normal_attack_reduces_hero_health(self):
        # test without spell and weapon
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=60)
        enemy.x = 3
        enemy.y = 2
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(h.health, 40)

    def test_enemy_with_same_x_as_hero_and_y_in_range_to_attack_choose_normal_attack_reduces_hero_health_2(self):
        # test with spell only and enemy dmg > spell dmg
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=60)
        enemy.x = 3
        enemy.y = 2
        s = Spell('fireball', damage=45, mana_cost=15, cast_range=3)
        enemy.learn(s)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(h.health, 40)

    def test_enemy_with_same_x_as_hero_and_y_in_range_to_attack_choose_normal_attack_reduces_hero_health_3(self):
        # test with weapon only and enemy dmg > weapon dmg
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=60)
        enemy.x = 3
        enemy.y = 2
        weapon = Weapon(name='Pruchka', damage=50)
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(h.health, 40)

    def test_enemy_with_same_x_as_hero_and_y_in_range_to_attack_choose_normal_attack_reduces_hero_health_4(self):
        # test with weapon and spell and enemy dmg > weapon dmg > spell dmg
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=60)
        enemy.x = 3
        enemy.y = 2
        weapon = Weapon(name='Pruchka', damage=50)
        s = Spell('fireball', damage=45, mana_cost=15, cast_range=3)
        enemy.learn(s)
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(h.health, 40)

    def test_enemy_with_same_x_as_hero_and_y_in_range_to_attack_choose_normal_attack_reduces_hero_health_5(self):
        # test with weapon and spell and enemy dmg > spell dmg > weapon dmg
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=60)
        enemy.x = 3
        enemy.y = 2
        weapon = Weapon(name='Pruchka', damage=50)
        s = Spell('fireball', damage=45, mana_cost=15, cast_range=3)
        enemy.learn(s)
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(h.health, 40)

    def test_enemy_with_bigger_weapon_dmg_and_not_enough_range_should_change_x_to_hero(self):
        # hero is on the right side of enemy and in the same y level
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=20)
        enemy.x = 1
        enemy.y = 3
        weapon = Weapon(name='Pruchka', damage=50)
        s = Spell('fireball', damage=45, mana_cost=15, cast_range=1)
        enemy.learn(s)
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(enemy.x, 2)

    def test_enemy_with_bigger_weapon_dmg_and_not_enough_range_should_change_x_to_hero_2(self):
        # hero is on the left side of enemy and in the same y level
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=20)
        enemy.x = 5
        enemy.y = 3
        weapon = Weapon(name='Pruchka', damage=50)
        s = Spell('fireball', damage=45, mana_cost=15, cast_range=1)
        enemy.learn(s)
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(enemy.x, 4)

    def test_enemy_with_bigger_weapon_dmg_and_not_enough_range_should_change_y_to_hero(self):
        # hero is on the same x as enemy but on lower y level
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=20)
        enemy.x = 3
        enemy.y = 1
        weapon = Weapon(name='Pruchka', damage=50)
        s = Spell('fireball', damage=45, mana_cost=15, cast_range=1)
        enemy.learn(s)
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(enemy.y, 2)

    def test_enemy_with_bigger_weapon_dmg_and_not_enough_range_should_change_y_to_hero_2(self):
        # hero is on the same x as enemy but on higher y level
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=20)
        enemy.x = 3
        enemy.y = 5
        weapon = Weapon(name='Pruchka', damage=50)
        s = Spell('fireball', damage=45, mana_cost=15, cast_range=1)
        enemy.learn(s)
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(enemy.y, 4)

    def test_enemy_with_bigger_spell_dmg_and_not_enough_range_should_change_x_to_hero(self):
        # hero is on the right side of enemy and in the same y level
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=20)
        enemy.x = 1
        enemy.y = 3
        weapon = Weapon(name='Pruchka', damage=0)
        s = Spell('fireball', damage=50, mana_cost=15, cast_range=1)
        enemy.learn(s)
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(enemy.x, 2)

    def test_enemy_with_bigger_spell_dmg_and_not_enough_range_should_change_x_to_hero_2(self):
        # hero is on the left side of enemy and in the same y level
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=20)
        enemy.x = 5
        enemy.y = 3
        weapon = Weapon(name='Pruchka', damage=0)
        s = Spell('fireball', damage=45, mana_cost=15, cast_range=1)
        enemy.learn(s)
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(enemy.x, 4)

    def test_enemy_with_bigger_spell_dmg_and_not_enough_range_should_change_y_to_hero(self):
        # hero is on the same x as enemy but on lower y level
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=20)
        enemy.x = 3
        enemy.y = 1
        weapon = Weapon(name='Pruchka', damage=0)
        s = Spell('fireball', damage=45, mana_cost=15, cast_range=1)
        enemy.learn(s)
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(enemy.y, 2)

    def test_enemy_with_bigger_spell_dmg_and_not_enough_range_should_change_y_to_hero_2(self):
        # hero is on the same x as enemy but on higher y level
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=20)
        enemy.x = 3
        enemy.y = 5
        weapon = Weapon(name='Pruchka', damage=0)
        s = Spell('fireball', damage=45, mana_cost=15, cast_range=1)
        enemy.learn(s)
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(enemy.y, 4)

    def test_enemy_with_bigger_basic_dmg_and_not_enough_range_should_change_x_to_hero(self):
        # hero is on the right side of enemy and in the same y level
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=60)
        enemy.x = 1
        enemy.y = 3
        weapon = Weapon(name='Pruchka', damage=0)
        s = Spell('fireball', damage=0, mana_cost=15, cast_range=1)
        enemy.learn(s)
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(enemy.x, 2)

    def test_enemy_with_bigger_basic_dmg_and_not_enough_range_should_change_x_to_hero_2(self):
        # hero is on the left side of enemy and in the same y level
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=20)
        enemy.x = 5
        enemy.y = 3
        weapon = Weapon(name='Pruchka', damage=0)
        s = Spell('fireball', damage=0, mana_cost=15, cast_range=1)
        enemy.learn(s)
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(enemy.x, 4)

    def test_enemy_with_bigger_basic_dmg_and_not_enough_range_should_change_y_to_hero(self):
        # hero is on the same x as enemy but on lower y level
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=20)
        enemy.x = 3
        enemy.y = 1
        weapon = Weapon(name='Pruchka', damage=0)
        s = Spell('fireball', damage=0, mana_cost=15, cast_range=1)
        enemy.learn(s)
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(enemy.y, 2)

    def test_enemy_with_bigger_basic_dmg_and_not_enough_range_should_change_y_to_hero_2(self):
        # hero is on the same x as enemy but on higher y level
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        enemy = Enemy(health=100, mana=40, damage=20)
        enemy.x = 3
        enemy.y = 5
        weapon = Weapon(name='Pruchka', damage=0)
        s = Spell('fireball', damage=0, mana_cost=15, cast_range=1)
        enemy.learn(s)
        enemy.equip(weapon)
        fight = Fight(enemy)
        h.x = 3
        h.y = 3
        fight.enemy_move(h)
        self.assertEqual(enemy.y, 4)


class TestMoveEnemyOneStep(unittest.TestCase):

    def test_with_same_y_level_and_hero_on_the_left_should_reduce_enemy_x_with_1(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        h.x = 1
        h.y = 3
        enemy = Enemy(health=100, mana=40, damage=20)
        enemy.x = 3
        enemy.y = 3
        fight = Fight(enemy)
        fight.move_enemy_one_step(h)

        expected_x = 2

        self.assertEqual(enemy.x, expected_x)

    def test_with_same_y_level_and_hero_on_the_right_should_increase_enemy_x_with_1(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        h.x = 5
        h.y = 3
        enemy = Enemy(health=100, mana=40, damage=20)
        enemy.x = 3
        enemy.y = 3
        fight = Fight(enemy)
        fight.move_enemy_one_step(h)

        expected_x = 4

        self.assertEqual(enemy.x, expected_x)

    def test_with_same_x_column_and_hero_is_above_enemy_should_reduce_enemy_y_with_1(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        h.x = 3
        h.y = 1
        enemy = Enemy(health=100, mana=40, damage=20)
        enemy.x = 3
        enemy.y = 3
        fight = Fight(enemy)
        fight.move_enemy_one_step(h)

        expected_y = 2

        self.assertEqual(enemy.y, expected_y)

    def test_with_same_x_column_and_hero_is_below_enemy_should_increase_enemy_y_with_1(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        h.x = 3
        h.y = 5
        enemy = Enemy(health=100, mana=40, damage=20)
        enemy.x = 3
        enemy.y = 3
        fight = Fight(enemy)
        fight.move_enemy_one_step(h)

        expected_y = 4

        self.assertEqual(enemy.y, expected_y)


if __name__ == '__main__':
    unittest.main()
