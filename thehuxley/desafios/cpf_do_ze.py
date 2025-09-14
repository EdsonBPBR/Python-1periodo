# O primeiro dígito de confirmação é calculado dada divisão # (somatório de Nj*i)/11, com j variando de 1 até 9, onde i = (11 - j) e Nj o número “j” dos nove fornecidos. # Se o resto for menor que dois então o ultimo digito será 0 (zero), caso contrário seu resto deverá ser subtraido de 11, gerando assim o primeiro dígito. # O segundo dígito de confirmação é calculado dada a divisão # (somatório de Nj*i)/11, com j variando de 1 até 10, onde i = (12 - j) e Nj o número “j” dos nove fornecidos mais o novo dígito. # Se o resto for menor que dois então o ultimo digito será 0 (zero), caso contrário seu resto deverá ser subtraído de 11, gerando assim o primeiro dígito.
def calculaVerificadores(cpf):
    cpf_com_dv1 = []

    # calcular o digito verificador 1, testei, está funcionando como blz.
    somatorio_dv1 = 0
    c = 10
    posicao = 0

    while c >= 2:
        somatorio_dv1 += int(cpf[posicao]) * c    
        cpf_com_dv1.append(cpf[posicao]) # fundamental para o calcula da DV2
        posicao += 1
        c -= 1
        
    resto_dv1 = somatorio_dv1 % 11

    if resto_dv1 < 2:
        DV1 = 0
    else:
        DV1 = 11 - resto_dv1
        
    cpf_com_dv1.append(str(DV1))

    posicao = 0 #reutilizar a variável no while da DV2

    # calculo da DV2, VERIFICADO TAMBÉM COM SUCESSO
    somatorio_dv2 = 0
    k = 11
    while k >= 2:
        somatorio_dv2 += int(cpf_com_dv1[posicao]) * k
        k -= 1
        posicao += 1

    resto_dv2 = somatorio_dv2 % 11

    if resto_dv2 < 2: 
        DV2 = 0
    else:
        DV2 = 11 - resto_dv2
    
    return DV1, DV2

def montaCPFcompleto(cpf, DV1, DV2):
    cpf_completo = ''
    for index_lista in range(9):
        cpf_completo += f'{cpf[index_lista]}'
        
    cpf_completo += f'-{DV1}{DV2}'
    
    return cpf_completo


if __name__ == '__main__':
    cpf_registrados = []
    m = int(input())

    for _ in range(m):
        cpf = str(input()).split()

        DV1, DV2 = calculaVerificadores(cpf)

        cpf_registrados.append(montaCPFcompleto(cpf, DV1, DV2))

    for registros in range(len(cpf_registrados)):
        print(f'Caso {registros+1}: {cpf_registrados[registros]}')