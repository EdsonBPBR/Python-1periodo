# Você deve ter duas funções (uma para o menor e outra para o maior) que recebem como parâmetro um ponteiro para o array.

c = 0
while c < 6:
    valor = int(input())
    if c == 0:
        maior = menor = valor
    else:
        if valor >= maior:
            maior = valor
        
        if valor <= menor:
            menor = valor
    c += 1

print(menor)
print(maior)

