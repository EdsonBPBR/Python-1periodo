def inverte_digito(digito):
    for caractere in digito[::-1]:
        print(f'[{caractere}]', end='')
    print()
    
def main():
    while True:
        digito = str(int(input()))
        if digito == '0':
            break
        inverte_digito(digito)

if __name__ == '__main__':
    main()