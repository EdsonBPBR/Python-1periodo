# Periodicamente as crianças brasileiras devem tomar vacinas que as protegem de diversas doenças. Escrever um programa para ler o ano em que a criança toma a 1a dose e a periodicidade (intervalo em anos) da vacina e exibir em que outros anos a criança deve tomar as próximas doses desta vacina, sabendo que são 4(quatro) doses ao total.

# A tabela abaixo traz exemplos de entrada e saída esperadas.

ano = int(input())
periodo = int(input())

c = ano
doses = 0 

while doses < 3:
    c += periodo
    print(c, end=" ")
    doses += 1
