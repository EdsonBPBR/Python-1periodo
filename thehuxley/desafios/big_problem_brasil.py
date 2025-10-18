while True:
    try:
        k, b = map(int, input().split())
        somatorio = 0

        while k > 0:
            somatorio += k%b
            if k//b <= 0:
                break
            k = k//b
            
        print(somatorio)
    except:
        break