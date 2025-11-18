class Cliente:
    def __init__(self, cpf, nome, celular):
        self._cpf = cpf
        self._nome = nome
        self._celular = celular
        
    def __str__(self):
        return f'{self._cpf} - {self._nome} - {self._celular}'
    
class ContaBancaria:
    def __init__(self, numero, cliente, limite):
        self._numero = numero
        self._cliente = cliente
        self._limite = limite
        self._saldo = 0.0
    
    def consultar_saldo(self):
        return self._saldo 
        
    def depositar(self, valor):
        self._saldo += valor
        
    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            return True
        return False
    
    def transferir(self, valor, conta_destino):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            return True
        return False
              
cliente1 = Cliente('123.456.789-70', 'Edson', '82993821363')
conta1 = ContaBancaria('1111', cliente1, 5000)
conta1.depositar(200)
print(conta1.consultar_saldo())
conta1.sacar(28)
print(conta1.consultar_saldo())
