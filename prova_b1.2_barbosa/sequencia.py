n = int(input())

padrao_a = 1

padrao_b = 1
x = 1

padrao_c = 1

print(f'{padrao_a} {padrao_b} {padrao_c}')

c = 0
while c < (n*2-1):

    print(f'{padrao_a} {padrao_b} {padrao_c}')

    if c % 2 == 0:
        padrao_a += 1
    
    if c % 2 == 0:
        padrao_b += 1
    else:
        x *= 2
        padrao_b += x

    if c % 2 == 0:
        padrao_c += 1
    else:
        padrao_c += c ** 2
    c += 1