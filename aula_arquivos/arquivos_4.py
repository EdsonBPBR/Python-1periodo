import pickle

with open("aula_arquivos/arquivos.txt", "wb") as arquivo: # escrita
    pickle.dump([1,2,3], arquivo)
    pickle.dump({1:"one", 2:"two"}, arquivo)
    
with open("aula_arquivos/arquivos.txt", "rb") as arquivo:  # leitura
    print(pickle.load(arquivo))
    print(pickle.load(arquivo))