class Produto:
    def __init__(self, codigo, nome, valor, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade
        self.total = valor*quantidade
        
    def __str__(self):
        return f'{self.codigo:^10} {self.nome:^10} {self.valor:^10} {self.quantidade:^5} {self.total:^12}'