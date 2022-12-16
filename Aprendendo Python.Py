print('Hello World')

"""
DocString
E escrever o que eu
quiser
asdfasdfd
"""

''' Usar para escrever suas notas '''

# Permite escrever um comentário
print(123)  # Na frente
# Abaixo
print(456)
# \r\n -> CRLF
# \n -> LF
print(12, 34, 1011, sep="....")
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')

"""
DocString
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos que estão dentro de aspas
"""
print(1234)

# Aspas simples
print("Luiz Otávio")
print(1, 'Luiz "Otávio"')

# Aspas duplas
print("Luiz Otávio")
print(2, "Luiz 'Otávio'")

# Escape
print("Luiz \"Otávio\"")

# r
print(r"Luiz \"Otávio\"")

# Tipos int e float
# int -> Número inteiro
# O tipo int representa qualquer número
# positivo ou negativo. int sem sinal é considerado
# positivo.
# print(11) # int
# print(-11) # int
# print(0)

# float -> Número com ponto flutuante
# O tipo float representa qualquer número
# positivo ou negativo com ponto flutuante.
# float sem sinal é considerado positivo.
# print(1.1, 10.11)
# print(0.0, -1.5)

# A função type mostra o tipo que o Python
# inferiu ao valor.
print(type('Otávio'))
print(type(0))
print(type(1.1), type(-1.1), type(0.0))

print(type(2 == 1))
print(1 == 1)
print(2 == 3)

# Tipo de dado bool (boolean)
# Ao questionar algo em um programa,
# só existem duas respostas possíveis:
# sim (True) ou não (False).
# Existem vários operadores para "questionar".
# Dentre eles o ==, que é um operador lógico que
# questiona se um valor é igual a outro
print(10 == 10)  # Sim => True (Verdadeiro)
print(10 == 11)  # Não => False (Falso)
print(type(True))
print(type(False))
print(type(10 == 10))
print(type(10 == 11))

# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')


# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculas, pode usar
# números e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para
# atribuir um valor a um nome (variável).
# Uso: nome_variavel = expressão

# nome_completo = 'Luiz Otávio Miranda'
# soma_dois_mais_dois = 2 + 2
# int_um = bool('1')
# print(int_um, type(int_um))
# print(nome_completo, soma_dois_mais_dois)
""""""
nome = 'Luiz'
idade = 17
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade:', idade)
print('É maior?', maior_de_idade)

nome = 'Luiz Otávio'
sobrenome = 'Miranda'
idade = 18
ano_nascimento = 2022 - idade
maior_de_idade = idade >= 18
altura_metros = 1.80

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)


print('      ')
print('      ')
print('      ')
adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

divisao = 10 / 3  # float
print('Divisão', divisao)

divisao_inteira = 10 // 3
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 55 % 2  # resto da divisão
print('Módulo', modulo)

print(10 % 8 == 0)
print(16 % 8 == 0)
print(10 % 2 == 0)
print(15 % 2 == 0)
print(16 % 2 == 0)
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)

nome = 'will'
altura = 1.75
peso = 75
imc = peso / (altura * altura)

print(nome, 'tem', altura, 'de altura', 'e seu peso é', peso)
print('o seu imc é', imc)


nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Luiz Otávio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987