def maiorDivisorComum(n1, n2):
    if n1 > n2:
        maior = n1
    else:
        maior = n2
    i = 1
    
    while i < maior:
        if n1 % i == 0 and n2 % i == 0:
            if i == 1:
                maior_divisor = i
            else:
                if i > maior_divisor:
                    maior_divisor = i
                    
                    return maior_divisor
        i += 1

n1 = int(input())
n2 = int(input())

print(maiorDivisorComum(n1, n2))

# if n1 > n2:
#     maior = n1
# else:
#     maior = n2
    
# i = 1
# while i < maior:
#     if n1 % i == 0 and n2 % i == 0:
#         if i == 1:
#             maior_divisor = i
#         else:
#             if i > maior_divisor:
#                 maior_divisor = i
#     i += 1
# print(maior_divisor)