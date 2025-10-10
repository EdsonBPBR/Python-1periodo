# Leia vários números até que o usuário digite 0.
# Depois, mostre:
# Quantos números foram digitados (sem contar o 0),
# E qual foi o maior número digitado.

# if __name__ == '__main__':
#     i = 0
#     while True:
#         try:
#             n = int(input("Digite um número: "))
            
#             if n == 0:
#                 break
            
#             if i == 0:
#                 maior = n
#             else:
#                 if n > maior:
#                     maior = n
#             i += 1
#         except ValueError:
#             print('Dado de entrada inválido! Informe valores inteiros, somente!')
            
#     print(f'Você digitou {i} números. O maior foi {maior}')
        
#outra resolução
if __name__ == '__main__':
    registros = []
    while True:
        try:
            n = int(input('Digite um número: '))
            
            if n == 0:
                break
            registros.append(n)
        except ValueError:
            print('Dado de entrada inválido! Informe valores inteiros, somente!')
            
    print(f'Você digitou {len(registros)} números. O maior foi {max(registros)}')