# Nos parques de diversão, alguns brinquedos tem idade e altura mínimas para poder andar neles. O parque Ambrolândia possui 3 brinquedos que possuem essa limitação: 
# Barca Viking: 1,5m de altura e 12 anos.
# Elevator of Death: 1,4m de altura e 14 anos.
# Final Killer: 1,7m de altura ou 16 anos. 
# Dada a altura e a idade de uma pessoa, faça um programa que identifique quantos brinquedos ele pode andar.

altura, idade = map(int, input().split())

n_brinquedos = 0

if (altura/100 >= 1.5) and idade >= 12:
    n_brinquedos += 1

if (altura/100 >= 1.4) and idade >= 14:
    n_brinquedos += 1
    
if (altura/100 >= 1.7) or idade >= 16:
    n_brinquedos += 1
    
print(n_brinquedos)