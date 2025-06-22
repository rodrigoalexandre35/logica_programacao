# Questão 1
nome = "Rodrigo"
idade = 35
print(f"Meu nome é {nome} e eu tenho {idade} anos.")

# Questão 2
a = 5
b = 10
a, b = b, a
print("Valor de a:", a)
print("Valor de b:", b)

# Questão 3
PI = 3.14159
raio = 4
area = PI * raio ** 2
print("Área do círculo:", area)

# Questão 4
inteiro = 10
decimal = 3.14
texto = "Python"
print("Tipo de inteiro:", type(inteiro))
print("Tipo de decimal:", type(decimal))
print("Tipo de texto:", type(texto))

# Questão 5
resultado = 10 + 5 * 2 - 3 ** 2
print("Resultado da expressão:", resultado)
# Explicação:
# 3 ** 2 = 9
# 5 * 2 = 10
# 10 + 10 - 9 = 11
# Ordem: potência > multiplicação > adição/subtração

# Questão 6
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura de {celsius}°C em Fahrenheit é {fahrenheit}°F")

# Questão 7
x = 3
y = 2
print("x e y são diferentes e maiores que zero:", x != y and x > 0 and y > 0)

# Questão 8
expressao = (5 > 3) and (2 < 1)
print("Resultado da expressão (5 > 3) and (2 < 1):", expressao)
# Explicação:
# (5 > 3) = True
# (2 < 1) = False
# True and False = False

# Questão 9
altura_str = "1.75"
altura_float = float(altura_str)
print(f"A altura convertida é: {altura_float}")

# Questão 10
alunos_python = {"Ana", "Bruno", "Carlos"}
alunos_java = {"Bruno", "Daniel", "Eva"}

print("Alunos que fazem as duas linguagens:", alunos_python & alunos_java)
print("Alunos que fazem só Python:", alunos_python - alunos_java)
print("Todos os alunos (sem repetição):", alunos_python | alunos_java)
