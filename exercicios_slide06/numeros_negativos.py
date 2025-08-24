# 8 (N ́umeros negativos) Crie um programa em Python para receber 10 n ́umeros do
# usu ́ario e informar quantos do valores digitados s ̃ao negativos.
#range(inicio, limite, incremento)
#range(0,10,1)

numeros_negativos = 0 #acumulador
for k in range(10):
    numero = float(input('Informe um número: '))

    if numero < 0:
        numeros_negativos += 1
    else:
        pass

print(f'Foram informados {numeros_negativos} números negativos')