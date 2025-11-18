class Produto:
    def __init__(self, descricao, preco):
       self._descricao = descricao
       self._preco = preco
       
    def __str__(self):
        return '{d} R${p:0.2f}'.format(
                                d=self._descricao,
                                p=self._preco)
  
          
# produto1 = Produto('sabonete', 2)
# print(produto1)