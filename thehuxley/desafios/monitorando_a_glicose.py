# Escreva um programa que receba como entrada os vários valores da taxa de glicose de Genival, até que o valor informado seja 0, e calcule a glicose média observada naquele dia.
# Caso esse valor seja inferior a 110, o programa deve exibir a mensagem Glicose Normal. Caso seja 200 ou mais, a mensagem exibida deve ser Glicose Muito Alta. Nos demais casos, o programa deve exibir Glicose Alterada.

def verificaGlicose(media_gligose):
    if media_gligose < 110:
        print('Glicose Normal')
    elif media_gligose > 200:
        print('Glicose Muito Alta')
    else:
        print('Glicose Alterada')

if __name__ == '__main__':
    c = 0
    somatorio_glicose = 0

    while True:
        glicose = int(input())
        
        if glicose == 0:
            break
        
        somatorio_glicose += glicose
        c += 1

    media_gligose = somatorio_glicose / c
    verificaGlicose(media_gligose)