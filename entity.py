from spell import Spell
from errors import LogicError

class Entity:
    def __init__(self, health, mana):
        self._max_health = float(health)
        self._max_mana = mana
        self._current_health = float(health)
        self._current_mana = mana
        self._weapon = None
        self._spell = None

    def is_alive(self):
        return self._current_health > 0

    @property
    def health(self):
        return self._current_health

    @property
    def mana(self):
        return self._current_mana

    def can_cast(self):
        if self._spell == None:
            return False
        if self._spell.mana_cost > self._current_mana:
            raise LogicError("No mana!")
        return True 
  
    def take_damage(self, damage):
        self._current_health -= damage
        if self._current_health < 0:
            self._current_health = 0

    def take_healing(self,healing_points):
        if not self.is_alive():
            return False
        if self._current_health + healing_points > self._max_health:
            self._current_health = self._max_health
        else:
            self._current_health += healing_points
        return True

    def take_mana(self, amount):
        self._current_mana += amount
        if self._current_mana > self._max_mana:
            self._current_mana = self._max_mana

    def equip(self,weapon):
        self._weapon = weapon

    def learn(self,spell):
        self._spell = spell

    def attack(self,by):
        if by == 'weapon':
            if self._weapon != None:
                return self._weapon.damage
        if by == 'magic':
            if self._spell != None:
                if self.can_cast(): 
                    return self._spell.damage
        return 0
