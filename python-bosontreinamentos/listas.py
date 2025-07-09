# n1 = [5,9,23,36,7,5,23]
# n2 = [2,8,10,13,22,25]
# valores = n1 + n2
# print(len(valores)) #tamanho da lista
# print(sorted(valores)) # sorted ordena a lista em ordem crescente
# print(sorted(valores, reverse=True)) #parâmetro reverse = True reverte a lista
# print(sum(valores)) #soma
# print(min(valores)) #valor minimo
# print(max(valores)) #máximo

# valores.append(13) #adicionar elemento na última posição
# valores.pop() #retira o último elemento da lista
# valores.pop(2) #retira o elemento que está na posição 2

# valores.insert(3, 21) #adiciona elemento na posição, argumento 1: posição (3), argumento 2: valor (21)

# print(12 in valores) #se existe um valor dentro da lista

planetas = ['Mercúrio', 'Vênus','Marte','Saturno', 'Urano', 'Netuno']
for planeta in planetas:
    print(planeta, end=' ')
