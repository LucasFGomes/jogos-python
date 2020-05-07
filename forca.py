def jogar():
    print("*********************************")
    print("** Bem vindo ao jogo da Forca! **")
    print("*********************************")

    palavra_secreta = 'banana'
    lista_letras_acertadas = []
    enforcou = False
    acertou  = False
    tamanho_palavra_secreta = len(palavra_secreta)

    print(f'A palavra secreta tem {tamanho_palavra_secreta} letras, Boa Sorte!')
    for letra in range(0, tamanho_palavra_secreta):
        lista_letras_acertadas.append("_")

    print(formatar_lista(lista_letras_acertadas))

    while(not enforcou and not acertou):
        chute = input('\nDigite uma letra: ')
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                lista_acertadas[index] = chute.upper()
            index += 1
        
        print(formatar_lista(lista_letras_acertadas))
        if (palavra_secreta.upper() == "".join(lista_letras_acertadas)):
            print(f"Parabéns, você acertou a palavra secreta: {palavra_secreta.upper()}!")
            break

    print("Fim de jogo")

def formatar_lista(lista): return " ".join(lista)

if __name__ == "__main__":
    jogar()