class Veiculo:
  def __init__(self, tipo, marca, ano, preco):
    self.tipo=tipo
    self.marca=marca
    self.ano=ano
    self.preco=preco

  def get_Tipo_V(self):
    return self.tipo
  
  def get_Marca_V(self):
    return self.marca

  def get_Ano_V(self):
    return self.ano

  def get_Preco_V(self):
    return self.preco
