'''
Fazer um programa que pergunte um número inteiro e apresente ao usuário
o antecessor e o sucessor do número informado.
'''

# Entrada de dados
num = int(input("Informe um número inteiro: "))

# Processamento de dados
antecessor = num - 1
sucessor = num + 1

# Sáida com os dados processados
print("O antecessor de ", num, "é ", antecessor)
print("O sucessor de ", num, "é ", sucessor)