hoteis_joao_pessoa = 0
campina_grande = 0
n_pousadas_tinto = 0
n = 0
for _ in range(10):
    tipo = str(input()).upper()
    estrelas = int(input())
    cidade = str(input()).upper()
    
    if tipo == 'HOTEL' and estrelas == 5 and cidade == 'JOÃO PESSOA':
        hoteis_joao_pessoa += 1
        
    if cidade == 'CAMPINA GRANDE':
        campina_grande += estrelas
        n += 1
        
    if tipo == 'POUSADA' and cidade == 'RIO TINTO':
        n_pousadas_tinto += 1

if n > 0:
    media = campina_grande / n
else:
    media = 0
    
print(hoteis_joao_pessoa)
print(int(media))
print(n_pousadas_tinto)