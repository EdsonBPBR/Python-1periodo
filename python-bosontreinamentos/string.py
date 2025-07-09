# email = input('Informe seu e-mail: ')
# arroba = email.find('@') #função find encontra algo dentro da string
# usuario = email[0:arroba]
# dominio = email[arroba+1:]

# if arroba == -1:
#     print('Email inválido!')
# else:
#     print('Email válido!')
    
# print(f'Nome do usuário: {usuario}')
# print(f'Domínio da instituição: {dominio}')

# produtos = 'Unicompra: melhores promoções! Até 50% de descontos'
# pos = produtos.find('compra')
# print(pos)
# print(produtos.capitalize()) #primeira letra da frase em maíscula
# print(produtos.title()) #cada letra de cada palavra em maísculo 

# n_produto = produtos.replace('descontos', 'descontos promocionais') #substituir 1 arg: o q deseja substituir, 2 arg: nova string

# frase = '             Brasil, patria amada!'
# print(frase.lstrip()) # elimina espaços da esquerda
# print(frase.rstrip()) #elimina espaços da  direita
# print(frase.strip()) #elimina os espaços da esquerda e direita

# frase_completa = 'O rato ruel a roupa do rei de Roma'
# print(frase_completa.ljust(20, "-")) #justificar a direita, passar como parâmetro o número de carateres a usar
# print(frase_completa.center(20))


# p = 'Edson Barros'
# print(p.startswith('Eds')) #começa com 'Eds'?? Retorna True ou false.  Recebe como argumentos o trecho em string, nesse caso 'Edson'
# print(p.endswith('rros')) #termina com 'rros'?? 

#Docstrings
"""
Docstring é uma espécie de documentação que podemos inserir dentro de um módulo, função ou classe no Python.
"""