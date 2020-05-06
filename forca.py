def jogar():
    print("*********************************")
    print("** Bem vindo ao jogo da Forca! **")
    print("*********************************")

    palavra_escreta = 'lucas'
    enforcou = False
    acertou  = False

    while(not enforcou and not acertou):

        chute = input('Digite uma letra: ')
        chute = chute.strip()

        index = 0
        for letra in palavra_escreta:
            if (chute.upper() == letra.upper()):
                print("A letra {} está na {} posição".format(letra, index))
            index += 1

    print("Fim de jogo")

if __name__ == "__main__":
    jogar()