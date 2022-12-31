import os


def main(user_name: str, rep: int = 10, *items: str):
    answer = input('Saisir votre nom d\'utilisateur :')
    croco = True
    number = 0

#    if user_name == answer and croco is True:
#        while number < rep:
#            number += 1
#            print('Hello boss bienvenue chez vous !')
#    else:
#        print('ALERTE !! ALERTE !! INTRUS !!')
#        os.system("ls -lah")

    try:
        assert user_name == answer and croco is True
    except AssertionError:
        print('ALERTE !! ALERTE !! INTRUS !!')
    else:
        while number < rep:
            number += 1
            print('Hello boss bienvenue chez vous !')

    for item in items:
        print(item)

