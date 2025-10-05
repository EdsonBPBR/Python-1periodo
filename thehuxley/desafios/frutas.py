# Você vai receber um número N (0 < N < 20), correspondendo ao número de testes.
# Para cada teste, você receberá duas linhas. A primeira linha contém um número de ponto flutuante V (0,10 ≤ V ≤ 20,00), indicando o montante gasto com a segunda linha contém o nome de cada fruta que Dona Marta comprou, separados por 
# espaço.

n = int(input())
valores = []
n_frutas = 0
n_valores = []
c = 0

while c < n:
   preco = float(input())
   dados = str(input()).split()
   
   valores.append(preco)
   n_frutas += len(dados)
   n_valores.append(len(dados))
   
   c += 1
   
for a in range(n):
    print(f'dia {a+1}: {n_valores[a]} kg')
print(f'{(n_frutas/n):.2f} kg por dia')
print(f'R$ {(sum(valores)/n):.2f} por dia')