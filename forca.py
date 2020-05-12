import random

def jogar():

    imprime_boas_vindas()
    palavra_secreta = carrega_palavra_secreta()
    tamanho_palavra_secreta = len(palavra_secreta)

    lista_letras_acertadas = inicializa_lista_acertadas(palavra_secreta)
    print(f'A palavra secreta tem {tamanho_palavra_secreta} letras, Boa Sorte!')
    print(formatar_lista(lista_letras_acertadas))

    enforcou = False
    acertou  = False
    total_chances = 7
    erros = 0

    while(not enforcou and not acertou):
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(palavra_secreta, chute, lista_letras_acertadas)
        else:
            erros += 1
            quant_chances = total_chances - erros
            print(f"Não existe essa letra na palavra secreta, agora você tem {quant_chances} tentativas.")
            desenha_forca(erros)

        enforcou = erros == total_chances 
        acertou = "_" not in lista_letras_acertadas
        print(formatar_lista(lista_letras_acertadas))

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def formatar_lista(lista): return " ".join(lista)

def imprime_boas_vindas():
    print("*********************************")
    print("** Bem vindo ao jogo da Forca! **")
    print("*********************************")

def carrega_palavra_secreta(nome_arquivo = 'palavras.txt', primeira_linha_valida = 0):
    palavras = []

    with open(nome_arquivo) as arquivo:
        for palavra in arquivo:
            palavras.append(palavra.strip())

    num_aleatorio = random.randrange(primeira_linha_valida, len(palavras))
    return palavras[num_aleatorio].upper()

def inicializa_lista_acertadas(palavra): 
    return ["_" for letra in palavra]

def pede_chute():
    chute = input('\nDigite uma letra: ')
    return chute.strip().upper()

def marca_chute_correto(palavra_secreta, chute, lista_letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            lista_letras_acertadas[index] = chute
        index += 1

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == "__main__":
    jogar()