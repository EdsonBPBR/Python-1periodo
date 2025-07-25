class Cliente:
    def __init__(self, nome, sobrenome, data_nascimento, email, celular, cidade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.email = email
        self.celular = celular
        self.cidade = cidade
    
    def __str__(self):
        return f'Olá, {self.nome} {self.sobrenome}!'