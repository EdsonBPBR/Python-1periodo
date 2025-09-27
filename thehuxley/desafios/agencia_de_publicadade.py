# A agência de publicidade Criativa prepara anúncios para seus clientes em vários tipos de mídia (rádio, tv, revista e outdoor). Seus preços variam de acordo com o que o ciente deseja:
# - Anúncios para rádio custam R$ 500 se for para FM, e R$ 300 se for para AM
# - Anúncios para TV custam R$ 1200 em horário regular (até 20h), e R$ 2000 em horário nobre (depois de 20h)
# - Anúncios para revista custam R$ 750, e para outdoor custam R$ 1500
# Escreva um programa que receba como entrada os dados dos anúncios escolhidos por 7 clientes da agência e exiba o total que ela vai receber e quantos anúncios de cada mídia 
    
if __name__ == '__main__':
    k = 0
    acumulo_lucro = 0

    while k < 7:
        tipo_anuncio = str(input()).upper()
        
        if tipo_anuncio == 'RÁDIO':
            tipo_radio = str(input()).upper()

            if tipo_radio == 'FM':
                acumulo_lucro += 500
            elif tipo_radio == 'AM':
                acumulo_lucro += 300
            else:
                print('Rádio Inválido!')

        elif tipo_anuncio == 'TV':
            horario_tv = str(input()).upper().split('H')
            hora = int(horario_tv[0])

            if hora > 20:
                acumulo_lucro += 2000
            else:
                acumulo_lucro += 1200
        
        elif tipo_anuncio == 'REVISTA':
            acumulo_lucro += 750
        
        elif tipo_anuncio == 'OUTDOOR':
            acumulo_lucro += 1500

        else:
            print('INVÁLIDO')

        k += 1

    print(f'{acumulo_lucro:.2f}')