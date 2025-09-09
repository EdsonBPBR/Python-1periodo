# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica e informe-o expresso no formato horas:minutos:segundos.

def calculaTempo(tempo = 0):
    hora = tempo // 3600
    resto_hora = tempo % 3600

    minutos = resto_hora // 60
    segundos = resto_hora % 60
    
    return f'{hora}:{minutos}:{segundos}'


if __name__ == '__main__':
    t = int(input())
    print(calculaTempo(t))