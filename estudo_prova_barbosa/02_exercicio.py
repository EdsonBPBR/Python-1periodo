# utilizando o método count
# lista = []
# while True:
#     n = int(input('Informe um número: '))
#     if n == 0:
#         break
#     lista.append(n)
    
# e = int(input('Informe um número inteiro que deseja buscar: '))
# print(f'O número inteiro {e} aparece {lista.count(e)} na lista de números inteiros')

# criando minha própria função
def main():
    lista = []
    while True:
        n = int(input('Informe um número: '))
        if n == 0:
            break
        lista.append(n)
        
    busca = int(input('Informe um número inteiro que deseja buscar: '))
    print(Contar(lista, busca))

def Contar(lista, busca):
    freq = 0
    for elemento in lista:
        if elemento == busca:
            freq += 1
            
    return freq

if __name__ == '__main__':
    main()