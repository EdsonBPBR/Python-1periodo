registros = []
nivel1 = []
nivel2 = []
nivel3 = []
nivel4 = []

while True:
    opc = int(input())
    
    if opc == 0:
        break
    
    elif opc == 1:
        descricao = str(input()).strip()
        nivel_priori = int(input())
        
        listas = {1: nivel1, 2: nivel2, 3: nivel3, 4: nivel4}
        
        listas[nivel_priori].append((nivel_priori, descricao))
    
    elif opc == 2:
        print(nivel1)
        print(nivel2) # dps eu tenho que imendar todas essas listas e ordenar elas
        print(nivel3)
        print(nivel4)
    
    else:
        pass
    