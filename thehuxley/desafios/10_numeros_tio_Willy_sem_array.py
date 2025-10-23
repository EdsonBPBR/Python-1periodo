while True:
    n = int(input())
    if n == -1:
        break
    
    c = 0
    freq = 0
    for i in range(10):
        m = int(input())
        if m == n:
            freq += 1
    print(f'{n} appeared {freq} times')