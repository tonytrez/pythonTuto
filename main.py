from Class.Thief import Thief
from Class.Warrior import Warrior
from Class.Wizard import Wizard

# import os
# from modules import player
# import modules.player

if __name__ == '__main__':
    # player.main('toto', 3, 'lolo', 'momo', 'clodo', 'clando')
    # modules.player.main('toto', 3, 'lolo', 'momo', 'clodo', 'clando')

    characterClass = input('Choisis la classe de ton personnage: \na. Voleur \nb. Guerrier \nc. Mage \n> ')
    try:
        if characterClass == 'a':
            character = Thief(10, 5, 10)
        elif characterClass == 'b':
            character = Warrior(10, 8, 5)
        elif characterClass == 'c':
            character = Wizard(10, 2, 10)
        else:
            raise AttributeError
    except AttributeError:
        print('Cette classe n\'existe pas, programme terminé')
    else:
        characterName = input('Quel est le nom de ton personnage ? ')
        character.name = characterName
        if isinstance(character, Thief):
            className = 'Voleur'
        elif isinstance(character, Warrior):
            className = 'Guerrier'
        else:
            className = 'Mage'
        print(
            "Bonjour {} tu es un {} avec {} point(s) de vie et {} point(s) de force".format(
                character.name, className, character.hp, character.power
            )
        )
        character.attack('momo')
