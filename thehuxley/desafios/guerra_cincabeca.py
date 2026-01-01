def verificaPrimo(n):
    if n == 2:
        print(1)
        return True
    
    if n <= 1 or n % 2 == 0:
        return False
    
    c = 0
    for k in range(3, int(n**0.5) + 1, 2): 
        if n % k == 0:
            c = 1
            break
    
    if c > 0:
        return False
    else:
        return True

def quadrado_perfeito(numero):
    if numero < 0:
        return False
    raiz = numero ** (1/2)
    if numero == raiz**2:
        return True
    return False

idade1, id1 = map(int, input().split())
nome1 = str(input())
pontuacao1 = 0
idade2, id2 = map(int, input().split())
nome2 = str(input())
pontuacao2 = 0

if verificaPrimo(idade1):
    pontuacao1 += 4
if verificaPrimo(idade2):
    pontuacao2 += 4

if quadrado_perfeito(id1):
    pontuacao1 += 3
if quadrado_perfeito(id2):
    pontuacao2 += 3
    
if len(nome1) > len(nome2):
    pontuacao1 += 2
else:
    pontuacao2 += 2
    
print(pontuacao1)
print(pontuacao2)

if pontuacao1 > pontuacao2:
    print(f'{nome1} WINS')
elif pontuacao2 > pontuacao1:
    print(f'{nome2} WINS')
else:
    print('CInCABECAS EMPATADOS')