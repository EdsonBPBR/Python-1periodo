while True:
    n = int(input())
    if n == 0:
        break
    
    if n < 0:
        print('Você ainda não nasceu.')
    elif (n >= 18 and n <= 70):
        print('Você tem a obrigatoriedade de votar.')    
    elif n > 70 or (n >= 16 and n < 18):
        print('Na sua idade, o voto é opcional. ')
    else:
        print('Você não pode votar.')