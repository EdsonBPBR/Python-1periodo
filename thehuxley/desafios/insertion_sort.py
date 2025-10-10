entrada = str(input()).split()
array = list(entrada)
print(array)

for posicao in range(len(array)):
    if posicao == (len(array)) - 1:
        print(f'{array[posicao]}', end = '')
    else:
        print(f'{array[posicao]}', end = ' ')
        
# 20 15 10 5 8 12 16
# 0  1  2  3 4 5  6

# 15 20 10 5 8 12 16
# 0  1  2  3 4 5  6

# 10 15 20 5 8 12 16

# 5 10 15 20 8 12 16
