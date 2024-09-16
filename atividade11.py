# Crie um programa que receba a idade de uma pessoa e classifique-a de acordo com as seguintes faixas etárias:
# Criança (0-12 anos)
# Adolescente (13-17 anos)
# Adulto (18-59 anos)
# Idoso (60 anos ou mais)

idade = int(input("Digite a idade: "))
if idade == 0 and idade <= 12:
    print("Criança")

elif idade >= 13 and idade <=1:
    print("Adolecente")

elif idade == 18 and idade <=59:
    print("Adulto")

elif idade >=60: 
    print("Idoso")