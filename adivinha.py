import random as rd

def jogo_adivinhacao():
    print('***********************')
    print('* Jogo de adivinhação *')
    print('***********************\n')

    nivel_str   = input('Escolha o nível de dificuldade: \n1 - Fácil\n2 - Normal\n3 - Difícil\n')

    nivel       = int(nivel_str)

    pontos      = 1000
    facil       = nivel == 1
    normal      = nivel == 2
    dificil     = nivel == 3

    if(facil):
        tentativa = 20
    elif(normal):
        tentativa = 10
    elif(dificil):
        tentativa = 3
    else:
        print('Por favor, escolha um nível adequado')

    comeco      = 1
    fim         = 100

    numero_secreto = rd.randrange(1, 101)

    for rodada in range(1, tentativa + 1):
        print('Tentativa {} de {}\n'.format(rodada, tentativa))
        chute_str = input('Digite um número de {} a {} \n'.format(comeco, fim))
        chute = int(chute_str)

        acerto  = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(chute < 1 | chute > 100):
            print('Por favor, digite um número entre {} e {}\n'.format(comeco, fim))
            continue

        if(acerto):
            print('Você acertou!\n')
            print('Sua pontuação é de {} pontos'.format(pontos))
            break
        else:
            if(maior):
                print('Número {} é maior!\n'.format(chute_str))
            elif(menor):
                print('Número {} é menor!\n'.format(chute_str))
            # Usando número absoluto
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            print('Perdeu {} pontos\n'.format(pontos_perdidos))
            print('Você fica com {} pontos restantes'.format(pontos))

    print('Final do jogo, o número era {}'.format(numero_secreto))

if(__name__ == "__main__"):
    jogo_adivinhacao()