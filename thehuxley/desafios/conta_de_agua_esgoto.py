# Faça um programa que receba a quantidade de m3 de água consumidos e o custo por litro de água e calcule:
# a) O valor a ser pago pela água; 
# b) O valor a ser pago pelo esgoto, sabendo que este corresponde a 80% do valor da água consumida;
# c) O valor total da conta, considerando água e esgoto.
# Dica: Lembre-se que 1 m3 = 1.000 litros

def AguaEesgoto(quantidade, custo):
        preco_agua = quantidade * custo * 1000
        esgoto = preco_agua * 0.8

        total = preco_agua + esgoto
        
        return preco_agua, esgoto, total


if __name__ == '__main__':
    quantidade, custo = map(float, input().split())
    preco_agua, esgoto, total = AguaEesgoto(quantidade, custo)

    print(f'{preco_agua:.2f}')
    print(f'{esgoto:.2f}')
    print(f'{total:.2f}')