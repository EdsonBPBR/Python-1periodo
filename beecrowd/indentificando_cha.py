cha = int(input())
entrada = str(input()).strip().split()
freq = 0
for i in range(len(entrada)):
    if int(entrada[i]) == cha:
        freq += 1
        
print(freq)