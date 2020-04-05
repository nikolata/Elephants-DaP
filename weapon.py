class Weapon:

    def __init__(self, name, damage):
        self._name = name
        self._damage = damage

    @property
    def damage(self):
        return self._damage

    @property
    def name(self):
        return self._name

    def __str__(self):
        return "Name: " + self.name + ", damage: " + str(self.damage)
