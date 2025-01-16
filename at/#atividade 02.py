#atividade 02

# Entrada de dados
numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))

# Cálculo do MDC usando algoritmo de Euclides
while numero_2 != 0:
    numero_1, numero_2 = numero_2, numero_1 % numero_2

print(f'MDC = {numero_1}')