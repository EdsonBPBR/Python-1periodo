def cadastra_sprinklers(registros, n_sprinkler, somatorio_temperatura):
    for _ in range(n_sprinkler):
        entrada = str(input()).split()
        somatorio_temperatura += float(entrada[1])
        registros.append({
            "id": int(entrada[0]),
            "temperatura": float(entrada[1]),
            "status": str(entrada[2])
        })

def verifica_sprinklers(registros):
    sprinkler_ativos = []
    for registro in registros:
        if not(registro['temperatura'] < 40 and registro['status'] == 'N' and registro['temperatura'] <= (somatorio_temperatura / n_sprinkler)*1.15):
            sprinkler_ativos.append(registro['id'])
    return sprinkler_ativos

def exibir_sprinklers_ativos(k):
    print(f'TESTE {k+1}')
    for sprinkler in verifica_sprinklers(registros):
        print(sprinkler) 

if __name__ == '__main__':
    registros = []
    t = int(input())
    for k in range(t):
        n_sprinkler = int(input())
        somatorio_temperatura = 0
        registros = []
        cadastra_sprinklers(registros, n_sprinkler, somatorio_temperatura)
        exibir_sprinklers_ativos(k)
        
# class Sprinkler:
#     def __init__(self, id, temperatura, fumaca):
#         self.id = id
#         self.temperatura = temperatura
#         self.fumaca = fumaca
        
# class SistemaSprinkler:
#     def __init__(self):
#         self.sprinklers = []
#         self.media_temperatura = 0
    
#     def adiciona_sprinkler(self, id, temperatura, status):
#         self.sprinklers.append({
#             "id": id,
#             "temperatura": temperatura,
#             "status": status
#         })
