# Ela traçou como meta depositar um valor X em seu cofrinho no primeiro dia da semana, e ir guardando a cada manhã o valor do dia anterior acrescido de pelo menos R$ 0,50. Mas será que ela vai conseguir fazer isso todos os dias?

n = 0
acumulador = 0
n_cumprimentos = 0
somatorio = 0

while n < 7:
    valor = float(input())
    somatorio += valor

    if n == 0:
        acumulador = valor

    else:
        if valor - acumulador >= 0.5:
            n_cumprimentos += 1
            acumulador = valor
        else:
            acumulador = valor

    n += 1 

print(f'R$ {somatorio:.2f}')
print(f'{n_cumprimentos}')
