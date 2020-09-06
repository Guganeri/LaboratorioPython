import random
import os

def jogar():
    print("*****************************")
    print("Bem-vindo ao jogo forca")
    print("*****************************")



    print(os.system("pwd"))
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo: 
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    print(palavra_secreta)
    
    letras_acertadas = ["_" for letra in palavra_secreta]
    erros = 0 

    enforcou = False
    acertou = False

    #enquanto não enforcou e não acertou
    while(not enforcou and not acertou):
        
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, Você errou ! faltam {} tentativas.".format(6-erros))

        enforcou = erros  == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    
    if (acertou):
        print("Você ganhou !!!")
    else:
        print("Você perdeu !!! D:")

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()