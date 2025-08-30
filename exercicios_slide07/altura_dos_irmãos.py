# (Altura dos irm ̃aos) Os irm ̃aos Jo ̃ao e Maria tˆem, respectivamente, 1.40m e 1.56m
# de altura. Jo ̃ao tem 10 anos e Maria tˆem 12 anos. Sabendo que Jo ̃ao cresce 1.8cm
# e Maria 1.2cm por ano, construa um programa que mostre com quantos anos Jo ̃ao
# e Maria estar ̃ao quando Jo ̃ao for mais alto que Maria.

# j(x) = 140 + 1,8x
# m(x) = 156 + 1,2x
# x = 80 / 3

# >>> ano = 80/3
# >>> joao = 140 + (1.8 * ano)
# >>> maria = 156 + (1.2 * ano)
# >>> joao == maria
# True

ano = 0
idade_joao = 10
idade_maria = 12
 
while True:
    ano += 1
    idade_joao += 1
    idade_maria += 1
    
    joao = 140 + (1.8 * ano) # ele tem 10 anos
    maria = 156 + (1.2 * ano) # ela tem 12 anos
    
    if joao > maria:
        print(joao, maria)
        print(f'João terá {idade_joao} e Maria terá {idade_maria}')
        break
    
    # print(joao, maria)
    # print(idade_joao, idade_maria)
    # input()
