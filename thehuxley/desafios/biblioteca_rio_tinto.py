def totalMulta(dias):
    return dias*0.75

def main():
    dias = int(input())
    print(f'{totalMulta(dias):.2f}')
    
if __name__ == '__main__':
    main()
