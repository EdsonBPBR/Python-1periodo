import secrets

c = 0
while c < 10:
    codigo = str(secrets.randbelow(10**6)).zfill(6) 
    print(codigo)
    
    input()