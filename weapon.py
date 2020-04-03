class Weapon:
    def __init__(self,name,damage):
        self._name = name
        self._damage = damage

    @property
    def damage(self):
        return self._damage
