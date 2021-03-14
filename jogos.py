import adivinha
import forca

def escolhe_jogo():
    print('**********************')
    print('* Escolha o seu jogo *')
    print('**********************\n')

    print('1 - Forca\n2 - Adivinhação\n')

    jogo = int(input('Qual jogo você quer jogar?\n'))

    if(jogo == 1):
        forca.jogo_forca()
    else:
        adivinha.jogo_adivinhacao()

if(__name__ == "__main__"):
    escolhe_jogo()