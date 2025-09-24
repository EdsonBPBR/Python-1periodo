# Você receberá um conjunto de dados contendo o nome da rua, número da residência, nome do bairro, cidade, estado e o número do cep (somente números). O programa deverá imprimir os dados conforme o modelo que os Correios utilizam para a postagem de correspondências.

nome_rua = str(input())
numero_residencia = str(input())
numero_bairro = str(input())
cidade = str(input())
estado = str(input())
numero_cep = str(input())

print(f"{nome_rua}, {numero_residencia}.")
print(f"Bairro: {numero_bairro}. Cep: {numero_cep}")
print(f"{cidade}/{estado}")