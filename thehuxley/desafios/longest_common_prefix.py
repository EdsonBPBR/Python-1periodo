# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

lista_palavras = ['carro', 'calhambeque', 'caminhão', 'edson'] # se não der certo, tentar fazer voltando, isso é, comparar edson, caminhão, calhambeque
semelhanca = ''

n_palavras = len(lista_palavras)
c = 0
while c < n_palavras:

    for index in range(len(lista_palavras[c])):
        print(lista_palavras[c][index], end='')
        
    input()
    c += 1
