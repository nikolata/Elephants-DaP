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
        if self._spell.get_mana_cost() > self._current_mana:
            return False
        return True 
    
    def take_damage(self, damage):
        self._current_health -= damage
        if self._current_health < 0:
            self._current_health = 0


    def take_healing(self,healing_points):
        if self._current_health == 0:
            return False
        if self._current_health + healing_points >100:
            self._current_health = 100
        else:
            self._current_health +=healing_points
        return True
    def equip(self,weapon):
        self._weapon = weapon
    def learn(self,spell):
        self._spell = spell

    def attack(self,by):
        if by == 'weapon':
            return self._weapon.damage
        if by == 'magic':
            return self._spell.damage
        else:
            return 0
