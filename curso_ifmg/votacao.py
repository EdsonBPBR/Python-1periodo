candidatos_cadastrados = {}
votos = {}

def cadastraCandidatos():
    while True:
        try:
            while True:
                nome = str(input('Nome candidato: '))
                if nome.upper() == 'SAIR':
                    break
                numero = str(input('Número do candidato: '))
                if numero.isdigit():
                    candidatos_cadastrados[numero] = nome
                else:
                    print('Número do candidato inválido!')
            break
        except ValueError:
            print('Número de candidatos inválido!')         

def exibirResultado(n_votos, votos, candidatos_cadastrados):
    for chave, total_votos in votos.items():
        porcentagem = (100 * total_votos) / n_votos
        if chave in candidatos_cadastrados:
            print(f'{candidatos_cadastrados[chave]} - {porcentagem:.2f}%')
        else:
            print(f'{chave} - {porcentagem:.2f}%')
        
if __name__ == '__main__':
    cadastraCandidatos()
    for chave in candidatos_cadastrados:
        votos[chave] = 0
    votos['nulos'] = 0
    votos['brancos'] = 0
    n_votos = 0

    while True:
        numero_candidato = str(input('Informe o número do candidato: '))
        if numero_candidato == 'TERMINAR':
            break
        
        if numero_candidato in candidatos_cadastrados:
            print(f'{numero_candidato:^20} - {candidatos_cadastrados[numero_candidato]:^20}')
            confirmar = str(input('Confirmar voto? S - SIM, N - NAO: ')).upper()
            
            if confirmar in ['S', 'SIM']:
                votos[numero_candidato] += 1
            elif confirmar in ['N', 'NAO']:
                votos["nulos"] += 1
            else:
                while confirmar not in ['S', 'SIM', 'N', 'NAO']:
                    confirmar = str(input('Confirmar voto? Informe: S - SIM, N - NAO: ')).upper()
                    if confirmar == 'S' or confirmar == 'SIM':
                        votos[numero_candidato] += 1
                        break
                    elif confirmar == 'N' or confirmar == 'NAO':
                        votos['nulos'] += 1
                        break
        else:
            if len(numero_candidato) == 0:
                votos['brancos'] += 1
                print('Voto em branco')
            else:
                votos['nulos'] += 1
                print('Voto nulo')       
        n_votos += 1 

    exibirResultado(n_votos, votos, candidatos_cadastrados)