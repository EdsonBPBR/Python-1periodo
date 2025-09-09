# Pedro notou que a quantidade de amigas de Perazzo que foram convidadas a comparecer ao evento dobra a cada minuto.Como todos os Expendables estão se preparando para a festa, Vivi pediu que você escrevesse um programa que o informasse a quantidade de amigas de Perazzo que confirmaram presença na festa, após um determinado tempo em minutos.

tempo = int(input())

resultado = 2 ** tempo
resultado_str = str(resultado)

for i in range(0, len(resultado_str), 50):
    print(resultado_str[i:i+50])
