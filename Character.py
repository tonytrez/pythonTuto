class Character:
    """
     Class Character
    """
    def __init__(self, hp: int = 10, power: int = 1):
        self._name: str
        self.hp = hp
        self.power = power

    def _getname(self):
        return self._name

    def _setname(self, name: str):
        while len(name) < 4:
            print("Your name must contain at least 4 letters")
            name = input("Quel est le nom de ton personnage ? ")

        self._name = name

    def attack(self, target: str):
        print('{} attaque {}'.format(self._name, target))

    name = property(_getname, _setname)
