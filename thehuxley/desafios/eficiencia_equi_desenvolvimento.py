# Escreva um programa que leia a quantidade de linhas de um programa (QUANTL), o número de funções existente nele (QUANTF), o tamanho da equipe (TAMEQ) e o número de bugs (NUMB) encontrados e calcule a eficiência da equipe de acordo com a seguinte formula: EFICIENCIA = (QUANTL / QUANTF) / TAMEQ – 4.2 x NUMB
# Utilize uma casa decimal de aproximação.
def calculaEficiencia(QUANTL, QUANTF, TAMEQ, NUMB):
    EFICIENCIA = ((QUANTL / QUANTF) / TAMEQ) - 4.2 * NUMB
    return EFICIENCIA

if __name__ == '__main__':
    QUANTL = int(input())
    QUANTF = int(input())
    TAMEQ = int(input())
    NUMB = int(input())

    print(f'{calculaEficiencia(QUANTL,QUANTF, TAMEQ, NUMB):.1f}')