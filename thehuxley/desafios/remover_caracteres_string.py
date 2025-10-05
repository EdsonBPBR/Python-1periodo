# Leia duas strings e retire da primeira string todas as letras que ocorrem na segunda string. Exemplo: Sejam as strings "chocolate" e "oca", então você deve imprimir "hlte"

entrada = str(input())
remover = str(input())

texto = list(entrada)

for sla in range(len(remover)):
    for x in texto[:]:   # percorre uma cópia
        if remover[sla] == x:
            texto.remove(x)

resul = ''     
for elementos in texto:
    resul += f'{elementos}' 
    
print(resul)
