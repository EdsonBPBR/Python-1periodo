import random
def escolhePalavra():
    lista_palavras_secretas = [
        'GEOMETRIA', 'COMPILADOR', 'INTERPRETADOR', 'BANCO DE DADOS', 'ALGORITMOS', 'PROGRAMACAO', 'ESTRUTURA DE DADOS', 'ARQUITETURA', 'HARDWARE', 'INFRAESTRUTURA'
        ]

    palavra_secreta = lista_palavras_secretas[random.randint(0,9)]
    return palavra_secreta




            
