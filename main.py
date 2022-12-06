from Veiculo import Veiculo
from Carro import Carro

Veiculo1= Veiculo('Moto', 'Honda', '2012', 8200)
Carro1 = Carro('Conversivel', 'Honda', '2015', 32000)

print("\n------------Veiculo no estabelecimento------------")
print(Veiculo1.get_Tipo_V(), Veiculo1.get_Marca_V(), Veiculo1.get_Ano_V(), Veiculo1.get_Preco_V())
print("\n--------------------------------------------------\n")

print("------------Carro no estabelecimento----------------\n")
print(Carro1.get_Tipo(), Carro1.get_Marca(), Carro1.get_Ano(), Carro1.get_Preco())
print("\n----------------------------------------------------")
