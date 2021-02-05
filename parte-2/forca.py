import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    arquivo = open("palavra.txt","r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero= erandom.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper();
   
    letras_acertadas = ["_" for letra in palavra_secreta];
    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = input("Qual letra?")
        chute = chute.strip().upper();

        if(chute in palavra_secreta):
            index =0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index = index +1;
        else:
            erros = erros +1;
        
        enforcou = erros == 6;
        acertou ="_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou")
    else:
        print("Você perdeu")
    print("fim do jogo")

if(__name__=="__main__"):
    jogar()