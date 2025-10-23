num = int(input())
real = float(input())
quant = 1

while abs(num) >= 10:
    num = num / 10
    quant += 1
print(quant)
