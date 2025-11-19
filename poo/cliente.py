class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        
    def exibir(self):
        print(f'{self.nome} - contato: {self.email}')
        
cliente1 = Cliente('Edson', 'barrosedson@gmail.com')
cliente1.exibir()