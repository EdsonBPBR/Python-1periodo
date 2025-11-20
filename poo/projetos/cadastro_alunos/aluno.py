class Aluno:
    def __init__(self, matricula, nome, idade, email):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        self.email = email
 
    def __str__(self):
        return f'MATRICULA: {self.matricula} | NOME: {self.nome} | IDADE: {self.idade} | E-MAIL: {self.email}'