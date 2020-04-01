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

if __name__ == '__main__':
    unittest.main()