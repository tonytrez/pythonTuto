from Character import Character


class Wizard(Character):
    """Class wizard"""
    def __init__(self, hp: int, power: int, mana: int):
        Character.__init__(self, hp, power)
        self.mana = mana
