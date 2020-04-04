from entity import Entity


class Hero(Entity):
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        super().__init__(health, mana)
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate
        self._x = None
        self._y = None

    def known_as(self):
        return f"{self.name} the {self.title}"

    def take_mana(self, amount):
        if amount is None:
            amount = self.mana_regeneration_rate
        super().take_mana(amount)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y
