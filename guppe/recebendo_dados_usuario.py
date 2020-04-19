import datetime

"""
Recebendo dados do usuário
input() -> Todo dado recebido via input é do tipo string
Em python, string é tudo que estiver entre:
- Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''
"""
# - Aspas dupla triplas -> """Angelina Jolie"""
"""
"""
# print("Qual seu nome:")
nome = input('Qual se nome?')
# Exemplo de print antigo Versão 2.x
# print('Seja bem-vindo(a) %s' % nome)
# Novo print versão 3.x
# print('Seja bem-vindo(a) {0}'.format(nome))
# Exemplo atual versão 3.6 acima
print(f'Seja bem vindo {nome}')
# print('Qual sua idade?')
idade = int(input('Qual sua idade?'))
# print('O(A) %s tem %s anos' % (nome, idade))
# print(f'A {nome} tem {idade} anos')
ano = datetime.date.today().year
print(f'A {nome} nasceu em {ano - idade}')
