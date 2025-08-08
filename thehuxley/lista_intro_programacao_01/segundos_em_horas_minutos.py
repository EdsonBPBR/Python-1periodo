#1h - 60 min
#1min - 60s
tempo_segundos = int(input('Informe o tempo em segundos(s): '))

horas = tempo_segundos // 3600 
resto_horas = tempo_segundos % 3600
minutos = resto_horas // 60 
segundos = resto_horas % 60  #os segundos equivalem ao resto da divisão

print(f'{horas} h {minutos} m {segundos} s')
# print(horas)
# print(minutos)
# print(segundos)
