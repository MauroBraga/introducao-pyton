import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

#numero_secreto =  round(random.random() * 100)
numero_secreto =  random.randrange(1,101)
total_de_tentativas = 3
rodada =1

print(numero_secreto)

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {} ".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu numero: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você acertou")
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
    rodada = rodada +1;

print("fim do jogo")