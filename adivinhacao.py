import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) fácil (2) médio (3) difícil")

    nivel = int(input("Defina o nível: "))
    if(nivel == 1):
        tentativas = 10
    elif(nivel == 2):
        tentativas = 5
    else:
        tentativas = 3

    for rodada in range(1, tentativas + 1):
        print("tentativa {} de {}".format(rodada, tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Voce digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("o número deve ser entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("voce acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("voce errou! o seu chute foi maior do que o numero secreto.")
            elif(menor):
                print("voce errou! Seu chute foi menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        print("---", pontos, "pontos ---")
        print("--- fim do jogo ---")

        if (__name__ == "__main__"):
            jogar()