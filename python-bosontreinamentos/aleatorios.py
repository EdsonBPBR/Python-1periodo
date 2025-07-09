from random import randint
import random

# for i in range(5):
#     valor =randint(1, 100)
#     print(valor, end=' ')

# função round realiza aproximações

lista = [5,7,8,9,11,56,58,8,12,56,4,1,2,3,6,9]
escolher_elemento = random.choice(lista)
escolher_elementos = random.sample(lista, 3) #especificar a quantidade de elementos que deseja buscar da lista 

embaralhar = random.shuffle(lista) #embaralhar os elementos da lista

print(escolher_elemento)
print(escolher_elementos)
print(embaralhar)