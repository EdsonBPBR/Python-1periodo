# Essa semana foi o Dia do Dentista e Vicente resolveu fazer uma doação de escovas de dente em uma creche de seu bairro. Depois de muito pesquisar, ele descobriu uma farmácia vendendo cada escova por R$ 2,20. Para a sorte de Vicente, essa mesma farmácia resolveu fazer uma promoção: comprando duas escovas, a terceira saía de graça.
# Escreva um programa que receba como entrada a quantidade de alunos da creche e exiba o valor total que ele gastará para comprar escovas para todos.

n = int(input())

if n > 0:
    c = 1
    for a in range(n, 0, -3):
        c += 1
        
        if a == 2:
            resultado = (c-1) * 4.4
            print(f'{resultado:.2f}')
            
        elif a == 1:
            resultado = ((c-2) * 4.4) + 2.2
            print(f'{resultado:.2f}')
        
        elif a == 3:
            resultado = (c-1) * 4.4
            print(f'{resultado:.2f}')
            
        else:
            pass
else:
    resultado = 0.00
    print(f'{resultado:.2f}')
