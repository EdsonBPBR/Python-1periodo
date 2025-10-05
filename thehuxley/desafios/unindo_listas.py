# Faça um programa para ler duas listas de valores inteiros e gerar uma terceira lista que seja a união das duas listas informadas pelo usuário.
# As listas devem ter pelo menos 1 elemento. Caso contrário, deve ser exibida a mensagem "Erro - A lista deve ter pelo menos 1 elemento."

n = int(input())

if n < 1:
    print("Erro - A lista deve ter pelo menos 1 elemento.")
else:
    a = []
    for _ in range(n):
        num = int(input())
        a.append(num)


    m = int(input())
    
    if m < 1:
        print("Erro - A lista deve ter pelo menos 1 elemento.")
    else:
        b = []
        for _ in range(m):
            num = int(input())
            b.append(num)
            
        c = a + b
        for elementos in c:
            print(elementos, end=' ')
    
