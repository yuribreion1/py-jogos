import random as rd

def jogo_forca():

    imprime_titulo()
    palavra = carrega_palavras()
    # Usando um laço for dentro de uma lista
    letras_acertadas = obter_letras_palavra(palavra)

    enforcou    = False
    acertou     = False
    erros       = 0

    while(not enforcou and not acertou):
        chutar = pedir_chute()
        if(len(chutar) > 1):
            print('Por favor digite apenas uma letra')

        if(chutar in palavra):
            chute_correto(palavra, chutar, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)
        print(letras_acertadas)

        # Encontrar uma letra ainda não encontrada
        acertou = '_' not in letras_acertadas

        enforcou = erros == 7
    
    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra)

def carrega_palavras():
    palavras = []

     # Leitura do arquivo
    arquivo = open('frutas.txt', 'r', encoding='UTF-8')
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = rd.randrange(0, len(palavras))

    palavra = palavras[numero].lower()
    quantidade_letras = len(palavra)
    return palavra

def chute_correto(palavra, chutar, letras_acertadas):
    index = 0
    for letra in palavra:
        if(chutar == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_titulo():
    print('*****************')
    print('* Jogo de Forca *')
    print('*****************\n')

def obter_letras_palavra(palavra):
    return ['_' for letra in palavra]

def pedir_chute():
    chute = input('Qual letra?\n').lower()
    chute = chute.strip()
    return chute

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogo_forca()