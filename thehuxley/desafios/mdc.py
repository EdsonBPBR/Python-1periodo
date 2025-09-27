
N = int(input())
M = int(input())

if N > M:
    maior = N
elif M > N:
    maior= M
else:
    maior = N

for a in range(1,maior+1):
    if a == 0:
        mdc = 1
    else:
        if N % a == 0 and M % a == 0:
            mdc = a

print(f'MDC={mdc}')