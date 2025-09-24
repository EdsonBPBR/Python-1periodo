# Faça um programa para corrigir automaticamente um conjunto de questionários. O programa deve receber primeiro o gabarito em uma única linha. Em seguida, o programa deve receber várias respostas de questionários e informar ao usuário o percentual de questões que ele acertou. O tamanho do questionário deve ser recebido no começo.

# O programa deve receber respostas de usuários até que o usuário digite "sair" no lugar da resposta.

# Se você receber um questionário de tamanho diferente do gabarito, você deve emitir uma mensagem de erro.

def verificaQuestionario(tamanho_gabarito, gabarito, gabarito_usuario):
    acertos = 0

    for index in range(tamanho_gabarito):
        if gabarito[index] == gabarito_usuario.split()[index]:
            acertos += 1
    porcentagem = (100 * acertos) / tamanho_gabarito

    return porcentagem

if __name__ == '__main__':
    tamanho_gabarito = int(input())
    gabarito = str(input()).split()

    if tamanho_gabarito == len(gabarito):
        while True:
            gabarito_usuario = str(input())
            
            if gabarito_usuario == 'sair':
                break

            elif len(gabarito_usuario.split()) != tamanho_gabarito:
                print('Tamanho da resposta diferente do tamanho do gabarito.')

            else:
                print(f"Percentual de acertos: {verificaQuestionario(tamanho_gabarito, gabarito, gabarito_usuario):.1f}")
        
    else:
        while tamanho_gabarito != len(gabarito):
            print('Gabarito de tamanho errado. Entre com o novo gabarito:')
            gabarito = str(input()).split()

        while True:
            gabarito_usuario = str(input())
            
            if gabarito_usuario == 'sair':
                break

            elif len(gabarito_usuario.split()) != tamanho_gabarito:
                print('Tamanho da resposta diferente do tamanho do gabarito.')

            else:
                print(f"Percentual de acertos: {verificaQuestionario(tamanho_gabarito, gabarito, gabarito_usuario):.1f}")