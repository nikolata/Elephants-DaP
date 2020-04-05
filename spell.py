class Spell:
    def __init__(self, name, damage, mana_cost, cast_range):
        self._name = name
        self._damage = damage
        self._mana_cost = mana_cost
        self._cast_range = cast_range

    @property
    def mana_cost(self):
        return self._mana_cost

    @property
    def damage(self):
        return self._damage

    @property
    def cast_range(self):
        return self._cast_range

    @property
    def name(self):
        return self._name

    def __str__(self):
        return ("Name: " + self._name + ", damage: " + str(self._damage) +
                ", mana_cost: " + str(self._mana_cost) + ", cast_range: " + str(self._cast_range))
