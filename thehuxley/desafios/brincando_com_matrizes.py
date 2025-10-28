somatorio_val_posi = 0
n_valores_posic = 0
somatorio_sem_diagonal = 0

for i in range(3):
    for j in range(3):
        elemento = int(input())
        if elemento > 0:
            somatorio_val_posi += elemento
            n_valores_posic += 1
            
        if i == 0 and j == 0:
            menor = elemento
        else: 
            if elemento < menor:
                menor = elemento
                
        if i != j:
            somatorio_sem_diagonal += elemento

media = somatorio_val_posi / n_valores_posic
if menor % 2 == 0:
    delta = 1
else:
    delta = 0
    
print(f'{media:.2f} {menor} {delta} {somatorio_sem_diagonal}')