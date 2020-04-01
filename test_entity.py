import unittest
from entity import Entity

class TestEntity(unittest.TestCase):
    def test_can_cast(self):
        pass

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

    def test_take_healing_when_healt_plus_healing_is_greather_than_100_hero_health_should_equal_100(self):
        healing = 80
        entity = Entity(health = 30, mana = 50)
        
        result = entity.take_healing(healing)
        self.assertEqual(entity._current_health,100)

    def test_take_healing_when_healt_plus_healing_is_lower_than_100_hero_health_should_equal_the_sum(self):
        healing = 50
        entity = Entity(health = 30, mana = 50)
        
        result = entity.take_healing(healing)
        self.assertEqual(entity._current_health,80)
    def test_take_healing_when_hero_is_alive_returns_True(self):
        healing = 50
        entity = Entity(health = 30, mana = 50)
        
        result = entity.take_healing(healing)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()