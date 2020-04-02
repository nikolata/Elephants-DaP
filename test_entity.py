import unittest
from entity import Entity
from spell import Spell
from errors import LogicError

class TestEntity(unittest.TestCase):
    def test_can_cast_with_no_spell_returns_false(self):
        entity = Entity(health = 100, mana = 50)

        self.assertFalse(entity.can_cast())

    def test_can_cast_with_not_enough_mana_raises_error(self):
        entity = Entity(health = 100, mana = 30)
        spell = Spell(name = "Fireball", damage = 30, mana_cost = 50, cast_range = 2)
        entity.learn(spell)

        with self.assertRaises(LogicError):
            entity.can_cast()

    def test_take_damage(self):
        damage = 20
        entity = Entity(health = 10, mana = 50)

        entity.take_damage(damage)

        self.assertEqual(0, entity.health)

    def test_take_healing_when_hero_is_dead_returns_false(self):
        healing = 30
        entity = Entity(health = 0, mana = 50)
        
        result = entity.take_healing(healing)
        self.assertFalse(result)

    def test_take_healing_when_health_plus_healing_is_greather_than_max_health_hero_health_should_equal_max_health(self):
        healing = 80
        entity = Entity(health = 30, mana = 50)
        
        result = entity.take_healing(healing)
        self.assertEqual(entity.health, 30)

    def test_take_healing_when_health_plus_healing_is_lower_than_max_health_hero_health_should_equal_the_sum(self):
        healing = 50
        damage = 70
        entity = Entity(health = 100, mana = 50)
        
        entity.take_damage(damage)
        result = entity.take_healing(healing)

        self.assertEqual(entity.health, 80)

    def test_take_healing_when_hero_is_alive_returns_True(self):
        healing = 50
        entity = Entity(health = 30, mana = 50)
        
        result = entity.take_healing(healing)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()