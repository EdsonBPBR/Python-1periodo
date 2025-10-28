import pickle

# with open('estudo_prova_barbosa/dados.dat', 'wb') as arquivo:
#     pickle.dump([], arquivo)

with open('estudo_prova_barbosa/dados.dat', 'rb') as arquivo:
    registros = pickle.load(arquivo)

print(registros)
registro = ['Edson', '1200000'] 
registros.append(registro)

with open('estudo_prova_barbosa/dados.dat', 'wb') as arquivo:
    pickle.dump(registros, arquivo)

with open('estudo_prova_barbosa/dados.dat', 'rb') as arquivo:
    registros = pickle.load(arquivo)
print(registros)