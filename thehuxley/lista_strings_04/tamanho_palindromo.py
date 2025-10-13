# Palíndromo é uma frase ou palavra que "se pode ler, indiferentemente, da esquerda para a direita ou vice-versa". Por exemplo, a palavra OSSO é palíndromo.
# O objetivo desta atividade é identificar se uma palavra ou frase é palíndromo, além de identificar o tamanho da substring (pedaço da palavra ou frase) que é duplicada. Por exemplo, o tamanho da substring duplicada de OSSO é 2.

# remover os espaços na entrada

# sopapos - 3 - 7 palavras
# reviver - 3 - 7 palavras
# redder - 3 - 6 palavras
# detartrated - 5 - 10 palavras
# amor e roma - 5 - 10 palavras

texto = str(input()).strip()

if texto.upper() == texto[::-1].upper():
    print('SIM')
    
    if len(texto) % 2 == 0:
        print(len(texto)//2)

    else:
        print((len(texto)//2) + 1)
else:
    print('NAO')