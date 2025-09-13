import random
def escolhePalavra():
    lista_palavras_secretas = [
        'INTELIGENCIA', 'COMPILADOR', 'INTERPRETADOR', 'MATEMATICA', 'ALGORITMOS', 'PROGRAMACAO', 'ESTRUTURA DE DADOS', 'ARQUITETURA', 'HARDWARE', 'INFRAESTRUTURA', 'SOFTWARE','RACIOCINIO', 'PROPEDEUTICA'
        ]

    palavra_secreta = lista_palavras_secretas[random.randint(0,9)]
    return palavra_secreta




            
