from utilitarios import (
    cadastrar_categoria,
    cadastrar_transacao,
    saldo_total
)

# cadastro de categorias
categoria_receitas = cadastrar_categoria('Receitas')
categoria_contas = cadastrar_categoria('Contas Fixas')
categoria_moto = cadastrar_categoria('Moto')
categoria_viagens = cadastrar_categoria('Viagens')

# cadastro de transações
cadastrar_transacao(
    descricao='Bolsa GIT novembro/2025',
    valor=1200,
    categoria=categoria_receitas
)

cadastrar_transacao(
    descricao='Bolsa CID novembro/2025',
    valor=700,
    categoria=categoria_receitas
)

cadastrar_transacao(
    descricao='Gasolina',
    valor=-100,
    categoria=categoria_moto
)

cadastrar_transacao(
    descricao='Conta de luz',
    valor=-175,
    categoria=categoria_moto
)

print(f'Saldo total: R$ {saldo_total()}')