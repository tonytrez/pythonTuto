def main():
    rep = 0
    user_name = "momo"
    answer = input('Saisir votre nom d\'utilisateur :')
    croco = True

    if user_name == answer and croco is True:
        while rep < 10:
            rep += 1
            print('Hello boss bienvenue chez vous !')
    else:
        print('ALERTE !! INTRUS !! INTRUS !!')


if __name__ == '__main__':
    main()
