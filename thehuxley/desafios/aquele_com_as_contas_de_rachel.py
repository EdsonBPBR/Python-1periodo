sacola = []
for _ in range(5):
    item = str(input()).strip()
    sacola.append(item)
input()
i = 0
for _ in range(6):
    tentativa = str(input()).strip()
    if  tentativa in sacola:
        i += 1
if i == 5:
    print('Could I be more happy?')
else:
    print('It is all just a moo point')
