"""
Tipo Float
Tipo Real, Decimal
Casas decimais
OBS: O separador de casas decimais na programação é o ponto e não a virgula.
"""

# Errado do ponto de vista do Float, mas gera uma tupla.
valor = 1, 44
print(valor)

# Certo do ponto de vista Float
valor = 1.44
print(valor)

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para inteiros.
"""
OBS: Ao converter valores float para inteiros, nos perdemos precisão.
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j
print(variavel)
print(type(variavel))