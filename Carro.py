from Veiculo import Veiculo

class Carro(Veiculo):
  def __init__(self, tipo, marca, ano, preco):
    super().__init__(tipo, marca, ano, preco)
    self.status=False

  def set_Status(self):
    self.status=True
    
  def get_Status(self):
    return self.status

  def get_Tipo(self):
    return self.tipo
  
  def get_Marca(self):
    return self.marca

  def get_Ano(self):
    return self.ano

  def get_Preco(self):
    return self.preco
