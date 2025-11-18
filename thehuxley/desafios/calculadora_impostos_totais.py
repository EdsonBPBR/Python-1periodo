cotacao_dolar = float(input())
aliquota = float(input())
valor_produto = float(input())
valor_frete = float(input())

vp = cotacao_dolar*valor_produto
v_frete = cotacao_dolar * valor_frete

if v_frete >= 2500:
    valor_total = vp + v_frete
    taxa = (valor_total-v_frete) * 0.6
    valor_final = (valor_total + taxa )/ (1-(aliquota/100))
    icms = valor_final*0.18
    total_impostos = icms + taxa
    total_produto = total_impostos + valor_total
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
else:
    valor_total = vp + v_frete
    taxa = valor_total * 0.6
    valor_final = (valor_total + taxa) / (1-(aliquota/100))
    icms = valor_final*0.18
    total_impostos = icms + taxa
    total_produto = total_impostos + valor_total

print(f'{cotacao_dolar:.2f}')
print(f'{vp:.2f}')
print(f'{v_frete:.2f}')
print(f'{valor_total:.2f}')
print(f'{taxa:.2f}')
print(f'{icms:.2f}')
print(f'{total_impostos:.2f}')
print(f'{total_produto:.2f}')