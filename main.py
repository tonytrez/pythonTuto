from Character import Character
# import os
# from modules import player
# import modules.player

if __name__ == '__main__':
    # player.main('toto', 3, 'lolo', 'momo', 'clodo', 'clando')
    # modules.player.main('toto', 3, 'lolo', 'momo', 'clodo', 'clando')
    characterName = input('Quel est le nom de ton personnage ? ')
    newCharacter = Character()
    newCharacter.name = characterName
    # os.system('clear')
    print(
        "Bonjour {} tu possedes {} point(s) de vie et {} point(s) de force".format(
            newCharacter.name, newCharacter.hp, newCharacter.power
        )
    )
