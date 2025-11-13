entrada = str(input()).strip().split()
array = []
for i in entrada:
    array.append(int(i))

print('Array original:')
for i in range(len(array)):
    if len(array) - 1 == i:
        print(f'{array[i]}\n', end='')
    else:
        print(array[i], end=' ')
    
array.sort()
array.reverse()
print('Array ordenado')
for i in range(len(array)):
    if len(array) - 1 == i:
        print(array[i], end='')
    else:
        print(array[i], end=' ')
        
        