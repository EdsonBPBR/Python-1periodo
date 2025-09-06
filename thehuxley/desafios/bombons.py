# Na bomboniere "Bombons" o próprio cliente faz suas caixas escolhendo a vontade entre os bombons de três tipos de recheios: avelã, caramelo e passas.

# Escrever programa para ler:

#     os preços das unidades de cada tipo de bombom: avelã, caramelo e passas, cada um em uma linha;
#     e a quantidade de cada bombom que o cliente deseja na caixa, na mesma ordem: avelã, caramelo e passas, também cada um em uma linha;

# E exibir o valor da caixa, com duas casas decimais.

p1 = int(input())
p2 = int(input())
p3 = int(input())

q1 = int(input())
q2 = int(input())
q3 = int(input())

print(f'Valor: R${(p1*q1 + p2*q2 + p3*q3):.2f}')