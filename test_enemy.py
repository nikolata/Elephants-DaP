import unittest
from enemy import Enemy
from weapon import Weapon
from spell import Spell


class TestEnemy(unittest.TestCase):

    def test_with_given_not_positive_health_raises_ValueError(self):
        with self.assertRaises(ValueError):
            Enemy(health=0, mana=40, damage=20)

    def test_with_given_negative_mana_raises_ValueError(self):
        with self.assertRaises(ValueError):
            Enemy(health=100, mana=-40, damage=20)

    def test_with_given_negative_damage_raises_ValueError(self):
        with self.assertRaises(ValueError):
            Enemy(health=100, mana=40, damage=-20)

    def test_if_enemy_is_created(self):
        enemy = Enemy(health=100, mana=40, damage=20)

        self.assertEqual(enemy.health, 100)
        self.assertEqual(enemy.mana, 40)
        self.assertEqual(enemy.damage, 20)

    def test_with_given_mana_potion_with_negative_value_raise_ValueError(self):
        enemy = Enemy(health=100, mana=40, damage=20)
        with self.assertRaises(ValueError):
            enemy.take_mana(-30)

    def test_if_take_mana_gains_the_mana_of_enemy(self):
        enemy = Enemy(health=100, mana=40, damage=20)
        enemy.take_mana(30)

        self.assertEqual(enemy.mana, 70)

    def test_if_enemy_attacks_with_personal_damage(self):
        enemy = Enemy(health=100, mana=40, damage=20)
        damage = enemy.attack()
        self.assertEqual(damage, enemy.damage)

    def test_with_given_weapon_enemy_attack_damage(self):
        enemy = Enemy(health=100, mana=40, damage=20)
        w = Weapon(name="The Axe of Destiny", damage=50)
        enemy.equip(w)
        damage = enemy.attack(by='weapon')
        self.assertEqual(damage, 50)

    def test_with_given_spell_enemy_attack_damage(self):
        enemy = Enemy(health=100, mana=60, damage=20)
        s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        enemy.learn(s)
        damage = enemy.attack(by='magic')

        self.assertEqual(damage, 30)

    def test_with_given_spell_and_not_enough_enemy_mana_raises_LogicError(self):
        enemy = Enemy(health=100, mana=20, damage=20)
        s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        enemy.learn(s)
        err = None
        try:
            enemy.attack(by='magic')
        except Exception as exc:
            err = exc

        self.assertIsNotNone(err)
        self.assertEqual(str(err), 'No mana!')


if __name__ == '__main__':
    unittest.main()
