# A SBC — Sociedade Brasileira de Copos — analisou estatísticas do treinamento de diversos garçons e descobriu que os garçons em treinamento deixam cair apenas bandejas que têm mais latas de bebidas que copos. Por exemplo, se uma bandeja tiver 10 latas e 4 copos, certamente o garçom em treinamento a deixará cair, quebrando os 4 copos. Já se a bandeja tiver 5 latas e 6 copos, ele conseguirá entregá-la sem deixar cair.

n = int(input())
quebrados = 0
c = 0
while c < n:
    entrada = str(input()).split()
    latas = int(entrada[0])
    copos = int(entrada[1])
    
    
    if latas > copos:
        quebrados += copos
    
    c += 1

print(quebrados)