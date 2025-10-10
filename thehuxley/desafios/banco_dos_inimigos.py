# Um inteiro X, representando a quantidade de personagens/monstros que constarão no banco.
# Os dados a serem colocados no banco:
# Uma sequencia de caracteres, que poderá ter no máximo 20 caracteres, representando um nome.
# 5 inteiros, representando ID, Level, Vida, Ataque e Defesa.

x = int(input())
registros = {}

for _ in range(x):
    nome = str(input())
    id = int(input())
    level = int(input())
    vida = int(input())
    ataque = int(input())
    defesa = int(input())
    
    registros[id] = [nome, level, vida, ataque, defesa]
    
for chave in registros.keys():
    print(f'Nome: {registros[chave][0]}')
    print(f'ID: {chave}')
    print(f'Level: {registros[chave][1]}')
    print(f'Vida: {registros[chave][2]}')
    print(f'Ataque: {registros[chave][3]}')
    print(f'Defesa: {registros[chave][4]}')