# Curso introdutório de Python - Initial Python course

Curso de Python 3 parte 1 na Alura - https://cursos.alura.com.br/course/python-3-introducao-a-nova-versao-da-linguagem

- Curso finalizedo em Março de 2021 - Course completed in March 2021
- [Certificado - Certificate](https://cursos.alura.com.br/certificate/a0b50593-b3e7-46ad-8123-4f72e8dd6180)

## Jogos disponíveis

1. Adivinhação
    - Consiste em um jogo simples de adivinhação, onde você escolhe inicialmente a dificuldade(que representa a quantidade de tentativas que você tem) e faz as suas tentativas.
        -   Fácil   - 20 tentativas
        -   Normal  - 10 tentativas
        -   Difícil - 3 tentativas
    
    Pontos legais que aprendi aqui:
    -   Estruturas de repetição
    -   Trabalhar com números absolutos
    -   Importação de módulos

2. Forca
    - Outro jogo de adivinhação baseado em uma lista de palavras vindas de um arquivo externo, permite você jogar em até 7 tentativas antes de se enforcar. 

    Pontos legais que aprendi aqui:
    -   Operação de I/O
    -   Uso de List Comprehension
    ``` python
        fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
        newlist = []
        for x in fruits:
        if "a" in x:
            newlist.append(x)
            
        print(newlist)
    ```
    -   Uso de funções e organização do código(encapsulamento)