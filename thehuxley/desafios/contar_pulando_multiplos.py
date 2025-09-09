# Sempre que Mariana faz alguma trela a professora a coloca de castigo, obrigando-a a escrever centenas de números. Para se distrair um pouco durante o castigo, a Mariana inventou uma pequena brincadeira: quando vai escrever os números, ela pula todos os múltiplos de 10. Escreva um programa que reproduza esse comportamento de Mariana.

numero = int(input())

c = 0
while c < numero:
    c += 1
    
    if c % 10 == 0:
        continue
    
    print(c) 
    