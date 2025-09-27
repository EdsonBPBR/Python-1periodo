# Construa um programa em C que receba uma quantidade de dias e converta esses dias para anos, semanas e dias. 

if __name__ == '__main__':
    dias = int(input())

    anos = dias // 365 
    resto_anos = dias % 365

    semana = resto_anos // 7 
    dia = resto_anos % 7

    print(f"{anos} ano(s), {semana} semana(s) e {dia} dia(s)")