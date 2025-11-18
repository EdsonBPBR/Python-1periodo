def constroiArray(entrada):
    array = []
    for i in range(len(entrada)):
        if len(entrada)-1 != i:
            array.append(int(entrada[i]))
    return array

def main():
    entrada = str(input()).split()
    lista = constroiArray(entrada)
    print(min(lista), max(lista))

if __name__ == '__main__':
    main()