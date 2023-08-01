'''
Elabore um programa que pergunte ao aluno suas 3 notas escolares.
O programa deverá calcular a média das 3 notas inseridos e exibir a média
'''

# Entrada de dados do usuário
n1 = float(input("Informe a sua primeira nota"))
n2 = float(input("Informe a sua segunda nota"))
n3 = float(input("Informe a sua terceira nota"))

# Processamento de dados
media = (n1 + n2 + n3) / 3

# Saída com os dados processados
print("Sua média é: {:.1f}".format(media))

# prog com decisão:

"""
n1 = float(input("Informe a sua primeira nota"))
n2 = float(input("Informe a sua segunda nota"))
n3 = float(input("Informe a sua terceira nota"))

media = (n1 + n2 + n3) / 3

print("Sua média é: {:.1f}".format(media))

if (media >=7)
    print("Você está aprovado)
else
    print("Você está reprovado)
"""