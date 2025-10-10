# No frigorífico do senhor Ambrósio, existem n bois. Cada boi traz preso em seu pescoço um cartão contendo seu número de identificação e seu peso. Faça um programa que escreva a identificação e o peso do boi mais gordo e do mais magro. Considere que os bois não têm pesos iguais.

if __name__ == '__main__':
    try:
        n = int(input())
        mais_gordo = []
        mais_magro = []

        def saida(mais_gordo, mais_magro):
            print(f'Gordo: id: {mais_gordo[0][0]} peso: {mais_gordo[0][1]:.2f}Kg')
            print(f'Magro: id: {mais_magro[0][0]} peso: {mais_magro[0][1]:.2f}Kg')
            
        for x in range(n):
            entrada = str(input()).split()
            id = int(entrada[0])
            peso = float(entrada[1])
            
            if x == 0:
                mais_gordo.append((id, peso)) # ainda fiquei perplexo porque o thehuxley não permitiu o uso das funções max e min
            else:
                if peso > mais_gordo[0][1]:
                    mais_gordo[0] = (id, peso)
            
            if x == 0:
                mais_magro.append((id, peso))
            else:
                if peso < mais_magro[0][1]:
                    mais_magro[0] = (id, peso)
                    
        saida(mais_gordo, mais_magro)
        
    except ValueError:
        print('Dado de entrada inválido! Informe um número inteiro!')