# Questão 1 - Operações com dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print("Soma:", num1 + num2)
print("Subtração:", num1 - num2)
print("Multiplicação:", num1 * num2)
print("Divisão:", num1 / num2 if num2 != 0 else "Divisão por zero não permitida")

# Questão 2 - Área do triângulo
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))
area = (base * altura) / 2
print("Área do triângulo:", area)

# Questão 3 - Salário mensal
ganho_hora = float(input("Quanto você ganha por hora? "))
horas_dia = float(input("Quantas horas trabalha por dia? "))
salario_mensal = ganho_hora * horas_dia * 5 * 4  # 5 dias por semana, 4 semanas
print("Salário mensal estimado:", salario_mensal)

# Questão 4 - Idade em dias
idade = int(input("Digite sua idade: "))
dias_vividos = idade * 365  # Desconsiderando anos bissextos
print("Você já viveu aproximadamente", dias_vividos, "dias.")

# Questão 5 - Nome completo
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
print("Nome completo:", nome, sobrenome)

# Questão 6 - Conversão Fahrenheit para Celsius e Kelvin
fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
kelvin = celsius + 273.15
print(f"Temperatura em Celsius: {celsius:.2f}°C")
print(f"Temperatura em Kelvin: {kelvin:.2f}K")

# Questão 7 - Contar quantidade de '1' na string
string_binaria = input("Digite uma string binária (ex: 1011001): ")
quantidade_uns = string_binaria.count('1')
print("Quantidade de 1's:", quantidade_uns)

# Questão 8 - Palavra invertida
palavra = input("Digite uma palavra: ")
print("Palavra invertida:", palavra[::-1])

# Questão 9 - Remover espaços de uma frase
frase = input("Digite uma frase com espaços: ")
sem_espacos = frase.replace(" ", "")
print("Frase sem espaços:", sem_espacos)

# Questão 10 - Inverter duas frases e trocar 'A' por '*'
frase1 = input("Digite a primeira frase: ")
frase2 = input("Digite a segunda frase: ")
frase1_modificada = frase1[::-1].replace('A', '*').replace('a', '*')
frase2_modificada = frase2[::-1].replace('A', '*').replace('a', '*')
print("Frase 1 modificada:", frase1_modificada)
print("Frase 2 modificada:", frase2_modificada)
