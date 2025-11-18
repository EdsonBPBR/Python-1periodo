class Cliente:
    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco
    
    def imprime(self):
        print(f'Cliente: {self._nome}')
        print(f'Endereço: {self._endereco}')
        
        
class Conta:
    _quant = 0
    
    @classmethod
    def adiciona_conta(cls):
        cls._quant += 1
        
    @classmethod
    def quantidade(cls):
        return cls._quant
    
    def __init__(self, numero, cliente):
        self.adiciona_conta()
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0.0
        
    def depositar(self, valor):
        self._saldo += valor
    
    def saldo(self):
        return self._saldo

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            return True
        return False
    
    def transferir(self, destino, valor):
        if self.sacar(valor):
            destino.depositar(valor)
            return True
        return False
    
cliente = Cliente('Edson', 'Sitio Acudinho')
conta1 = Conta(1111, cliente)
cliente = Cliente('Americanas', 'Minador')
conta2 = Conta(2222, cliente)
conta1.depositar(500)
conta2.depositar(100)