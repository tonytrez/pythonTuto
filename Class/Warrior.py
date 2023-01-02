from Character import Character


class Warrior(Character):
    """Class warrior"""
    def __init__(self, hp: int, power: int, shield: int):
        Character.__init__(self, hp, power)
        self.shield = shield

