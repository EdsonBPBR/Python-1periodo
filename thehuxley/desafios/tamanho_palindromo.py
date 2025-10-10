# O objetivo desta atividade é identificar se uma palavra ou frase é palíndromo, além de identificar o tamanho da substring (pedaço da palavra ou frase) que é duplicada. Por exemplo, o tamanho da substring duplicada de OSSO é 2.

# texto = str(input()).upper()

# if texto == texto[::-1]:
#     print('SIM')
#     for i in range(1, len(texto)//2 + 1):
#         if texto[:i] == texto[-i:]:
#             substring = texto[:i]
            
#     print(substring)
# else:
#     print('NAO')


texto = "AIBOFOBIA"

for i in range(1, len(texto)//2 + 1):
    print(texto[:i])
    print(texto[i:])