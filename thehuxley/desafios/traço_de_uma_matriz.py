# Na álgebra linear, o traço de uma matriz quadrada é a função matricial que associa a matriz à soma dos elementos da sua diagonal principal.

n = int(input())
somatorio = 0
elementos = []

for b in range(n):
    linha = str(input()).split()
    somatorio += float(linha[b])
    elementos.append(float(linha[b]))

st = ""
for a in range(len(elementos)):
    if len(elementos)-1 == a:
        st += f"({elementos[a]:.2f})"
    else: 
        st += f"({elementos[a]:.2f}) + "
    
print(f"tr(A) = {st} = {somatorio:.2f}")