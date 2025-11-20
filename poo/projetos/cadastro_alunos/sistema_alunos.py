class SistemaAlunos:
    def __init__(self):
        self.alunos_cadastrados = []
        
    def cadastrar_aluno(self, aluno): 
        self.alunos_cadastrados.append(aluno)
        
    def listar_alunos(self):
        return self.alunos_cadastrados
    
    def busca_aluno(self, matricula):
        for aluno in self.alunos_cadastrados:
            if aluno.matricula == matricula:
                return aluno
        return None