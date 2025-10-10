import os
# dá pra criar um gerenciador de arquivos com essas funções e métodos

diretorio = os.getcwd()

print(os.listdir(diretorio))

for arq in os.listdir(diretorio):
    if os.path.isfile(arq):
        print(arq)