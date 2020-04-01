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
    def get_health(self):
        return self._current_health

    @property
    def get_mana(self):
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


    

