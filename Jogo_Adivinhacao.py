import random

def jogar_adivinhacao():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = round(random.random()*100)
    rodada =1
    pontos = 1000 #defini uma pontuação inicial

    print("\nVocê tem 1000 pontos iniciais!")
    print("Qual nivel de dificuldade?")
    print("(1)facil (2)medio (3)dificil\n")
    nivel= int(input("defina o nivel: "))
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    # print(numero_secreto) | caso eu queira saber o numero gerado, colocar essa linha


    while(rodada <= total_de_tentativas):
        print("tentativa {} de {} ".format(rodada, total_de_tentativas))
        chute = input("Digite o seu numero: ")
        print("Você digitou: ", chute)

        numero = int(chute)
        acertou = numero_secreto == numero
        maior = numero >numero_secreto
        menor = numero<numero_secreto

        if(acertou):
            print("Vc acertou")
            print("Sua pontuação final foi {}".format(pontos))
            break
        else:
            if(maior):
                print("Vc errou. O seu chute foi maior que o numero secreto")
            elif(menor):
                print("Vc errou. O seu chute foi menor que o numero secreto")

        pontos_perdidos = abs(numero_secreto -numero)
        pontos = pontos - pontos_perdidos
        rodada = rodada + 1

    print("\nFim do jogo")
    print("O numero secreto é: {}".format(numero_secreto))

if(__name__== "__main__"):
    jogar_adivinhacao() #faz com que eu rode o programa tanto no próprio File quanto Importado


