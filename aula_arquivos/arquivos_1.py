# abrir o arquivo (open)
# ler / escrever no arquivo (write, read, readline, redlines)
# fechar o arquivo (close)

# w
# r (read)
# a (apend)
# r+

# titulo = str(input())
# arquivo = open("aula_arquivos/teste.txt", "a")
# arquivo.write(f"{titulo:^25} \n")
# arquivo.close()


# with open("aula_arquivos/teste.txt", "a") as arquivo: #escrita
#     arquivo.write("Linha 1 \n")
#     arquivo.write("Linha 2 \n")
#     arquivo.write("Linha 3 \n")
    
with open('aula_arquivos/teste.txt', 'r') as arquivo:
    a = arquivo.read() # ler o arquivo como um todo #readline, readlines()
    b = arquivo.readline()
    c = arquivo.readlines()
    print(a)
    print(c)

