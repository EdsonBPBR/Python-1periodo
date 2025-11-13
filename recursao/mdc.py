a = int(input())
b = int(input())
def mdc(a, b):
    resto = a % b
    if resto == 0:
        return b
    else:
        return mdc(b, resto)
print(mdc(a, b))
    
