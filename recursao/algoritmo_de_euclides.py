# # A = D*Q + R

# # mdc(36,24)
# # 12 é divisor de 36 e 24
# # portanto mdc(36,24) = mdc(24,12)

# # 36 = 24*1 + 12
# # 24 = 12*2 + 0
def mdc(a,d):
    resto = a % d
    if resto == 0:
        return d
    else:
        return mdc(d, resto)
def main():
    n = int(input())
    for _ in range(n):
        entrada = str(input()).split()
        a = int(entrada[0])
        d = int(entrada[1])
        print(f'MDC({a},{d}) = {mdc(a,d)}')
        
if __name__ == '__main__':
    main()