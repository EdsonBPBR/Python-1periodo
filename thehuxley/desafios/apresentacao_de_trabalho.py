# A apresentação de Programação 1 está chegando, e o Professor deixou claro que se os trabalhos não passassem por todos os requisitos mínimos, ele não iria julgar o trabalho.

# Eis os requisitos:

# Requisito 1: Inferface gráfica OU Inteligência Artificial.
# Requisito 2: Encapsulamento E Indentação.
# Requisito 3: Uso de Structs
print('Trabalho aborda Interface Grafica? (0 - Nao 1 - Sim)')
tig = int(input())

print('Trabalho aborda Inteligencia Artificial? (0 - Nao 1 - Sim)')
tia = int(input())

print('Trabalho aborda Encapsulamento? (0 - Nao 1 - Sim)')
te = int(input())

print('Trabalho aborda Indentacao? (0 - Nao 1 - Sim)')
ti = int(input())

print('rabalho aborda Structs? (0 - Nao 1 - Sim)')
ts = int(input())

if not(tig == 0 and tia == 0) and not(te == 1 and ti == 0 or te == 0 and ti == 1) and ts == 1:
    print('Seu trabalho sera avaliado.')
else:
    print('Seu trabalho nao sera avaliado, nota 0.')