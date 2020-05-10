import random

def jogar():
    print("*********************************")
    print("** Bem vindo ao jogo da Forca! **")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = [palavra.strip() for palavra in arquivo]
    arquivo.close()

    num_aleatorio = random.randrange(0, len(palavras))
    palavra_secreta = palavras[num_aleatorio].upper()

    lista_letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou  = False
    quant_chances = 6
    tamanho_palavra_secreta = len(palavra_secreta)

    print(f'A palavra secreta tem {tamanho_palavra_secreta} letras, Boa Sorte!')

    print(formatar_lista(lista_letras_acertadas))

    while(not enforcou and not acertou):
        chute = input('\nDigite uma letra: ')
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    lista_letras_acertadas[index] = chute
                index += 1
        else:
            quant_chances -= 1
            print(f"Não existe essa letra na palavra secreta, agora você tem {quant_chances} tentativas.")

        enforcou = quant_chances == 0 
        acertou = "_" not in lista_letras_acertadas
        print(formatar_lista(lista_letras_acertadas))

    if (acertou):
        print(f"Parabéns, você acertou a palavra secreta: {palavra_secreta}!")
    else:
        print(f"Que pena, você perdeu! A palavra secreta era: {palavra_secreta}")

    print("Fim de jogo")

def formatar_lista(lista): return " ".join(lista)

if __name__ == "__main__":
    jogar()