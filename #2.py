#2
# Solicitar o valor do saque ao usuário
valor = float(input("Digite o valor do saque (em R$): "))

# Inicializar as variáveis para cada cédula e moeda
notas_100 = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_5 = 0
notas_2 = 0
moedas_1 = 0
moedas_50 = 0
moedas_25 = 0
moedas_10 = 0
moedas_5 = 0
moedas_1_centavo = 0

# Calcular as cédulas de R$ 100,00
notas_100 = int(valor // 100)
valor %= 100

# Calcular as cédulas de R$ 50,00
notas_50 = int(valor // 50)
valor %= 50

# Calcular as cédulas de R$ 20,00
notas_20 = int(valor // 20)
valor %= 20

# Calcular as cédulas de R$ 10,00
notas_10 = int(valor // 10)
valor %= 10

# Calcular as cédulas de R$ 5,00
notas_5 = int(valor // 5)
valor %= 5

# Calcular as cédulas de R$ 2,00
notas_2 = int(valor // 2)
valor %= 2

# Calcular as moedas de R$ 1,00
moedas_1 = int(valor // 1)
valor %= 1

# Calcular as moedas de R$ 0,50
moedas_50 = int(valor // 0.50)
valor %= 0.50

# Calcular as moedas de R$ 0,25
moedas_25 = int(valor // 0.25)
valor %= 0.25

# Calcular as moedas de R$ 0,10
moedas_10 = int(valor // 0.10)
valor %= 0.10

# Calcular as moedas de R$ 0,05
moedas_5 = int(valor // 0.05)
valor %= 0.05

# Calcular as moedas de R$ 0,01
moedas_1_centavo = int(round(valor // 0.01))

# Exibir a quantidade de notas e moedas
print("\nResultado do saque:")
if notas_100 > 0:
    print(f"Cédulas de R$ 100,00: {notas_100}")
if notas_50 > 0:
    print(f"Cédulas de R$ 50,00: {notas_50}")
if notas_20 > 0:
    print(f"Cédulas de R$ 20,00: {notas_20}")
if notas_10 > 0:
    print(f"Cédulas de R$ 10,00: {notas_10}")
if notas_5 > 0:
    print(f"Cédulas de R$ 5,00: {notas_5}")
if notas_2 > 0:
    print(f"Cédulas de R$ 2,00: {notas_2}")
if moedas_1 > 0:
    print(f"Moedas de R$ 1,00: {moedas_1}")
if moedas_50 > 0:
    print(f"Moedas de R$ 0,50: {moedas_50}")
if moedas_25 > 0:
    print(f"Moedas de R$ 0,25: {moedas_25}")
if moedas_10 > 0:
    print(f"Moedas de R$ 0,10: {moedas_10}")
if moedas_5 > 0:
    print(f"Moedas de R$ 0,05: {moedas_5}")
if moedas_1_centavo > 0:
    print(f"Moedas de R$ 0,01: {moedas_1_centavo}")
