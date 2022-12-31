class Character:
    """
     Class Character
    """
    def __init__(self, name: str, hp: int = 10, power: int = 1):
        self.name = name
        self.hp = hp
        self.power = power

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name
