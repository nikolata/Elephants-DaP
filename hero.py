from entity import Entity


class Hero(Entity):
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        super().__init__(health, mana)
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate

    def known_as(self):
        return f"{self.name} the {self.title}"

    def take_mana(self, amount):
        if amount is None:
            amount = self.mana_regeneration_rate
        super().take_mana(amount)
