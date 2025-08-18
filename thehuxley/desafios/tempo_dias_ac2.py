# Faça programa que recebe um tempo dado em segundos e calcula quantos dias, horas, minutos e segundos ele representa.

tempo = int(input('(s): '))

dia = tempo // 86400
resto_dia_seg = tempo % 86400
hora = resto_dia_seg // 3600
resto_hora_seg = resto_dia_seg % 3600
minutos = resto_hora_seg // 60
segundos = resto_hora_seg % 60

print(dia)
print(hora)
print(minutos)
print(segundos)
