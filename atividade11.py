# Crie um programa que receba a idade de uma pessoa e classifique-a de acordo com as seguintes faixas etárias:
# Criança (0-12 anos)
# Adolescente (13-17 anos)
# Adulto (18-59 anos)
# Idoso (60 anos ou mais)

idade = int(input("qual sua idade: "))

# Criança (0-12 anos)

if (idade<=12):
    print("você é criança")

# Adolescente (13-17 anos)

elif (idade<=17):
    print("você é um adolescente")

# Adulto (18-59 anos)

elif (idade<=59):
    print("você é adulto")

# Idoso (60 anos ou mais)

elif (idade>=60):
    print("você é idoso")