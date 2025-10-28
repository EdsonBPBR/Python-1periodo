a = 0 # eu posso printar
b = 1 # eu posso printar
s1 = a + b # # eu posso printar
s2 = s1 + b # eu posso printar

termo_anterior = 1 # fiquei pensando: se o usuário digitar N = 0, imprimir nada, se o usuário informar N = 1, imprimir 0, se N == 2, 0, 1, se N == 3: 0, 1, 1, se N == 4, (0,1,1,2) se N == 5 aí entra no laço de repetiação (0,1,1,2,3)
termo_sucessor = 2

c = 0
while True:
    # if c == 0:
    #     termo_anterior = 0
    #     termo_sucessor = 1
    #     s = termo_anterior + termo_sucessor
    #     print(termo_anterior)
    # elif c == 1:
        
    # else:
    #     s = termo_anterior + termo_sucessor
    # print(s)
    s = termo_anterior + termo_sucessor
    termo_anterior = termo_sucessor
    termo_sucessor = s
    print(s)
    input()
    c += 1
    


