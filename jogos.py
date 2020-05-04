import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("******* Escolha seu jogo! *******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    escolha = int(input("Qual jogo? "))

    if (escolha == 1):
        print("Jogando Forca...")
        forca.jogar()
    elif (escolha == 2):
        print("Jogando Adivinhação...")
        adivinhacao.jogar()

if __name__ == "__main__":
    escolhe_jogo()