# Faça um programa que calcule o valor da hipotenusa de acordo com o teorema de pitágoras. Você não precisa se preocupar com casos em que os catetos fornecidos não podem formar um triângulo.

# Pesquise como fazer a operação de raiz quadrada.

# Todos os valores fornecidos dão resultados inteiros
def calculaHipotenusa(cat_a, cat_b):
    
    """"
    Calcula a hipotenusa e deve retornar um valor INTEIRO
    >>> calculaHipotenusa(0.84, 2.88)
    3
    >>> calculaHipotenusa(3.0, 4.0)
    5
    >>> calculaHipotenusa(6.0, 8.0)
    10
    """

    x = (cat_a**2) + (cat_b**2)
    hipo = x ** (0.5)

    return int(hipo)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
