from Character import Character


class Thief(Character):
    """Class thief"""
    def __init__(self, hp: int, power: int, stamina: int):
        Character.__init__(self, hp, power)
        self.stamina = stamina
