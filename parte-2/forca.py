import random

def pede_chute():
    chute = input("Qual letra?")
    chute = chute.strip().upper();
    return chute;

def jogar():
    
    imprime_mensagem_abertura();

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acetadas(palavra_secreta);
    enforcou = False
    acertou = False
    erros = 0


    while(not enforcou and not acertou):
        chute = pede_chute();

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



def imprime_mensagem_abertura():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palavra.txt","r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero= random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper();
    return palavra_secreta;

def inicializa_letras_acetadas(palavra):
   return  ["_" for letra in palavra]

if(__name__=="__main__"):
    jogar()