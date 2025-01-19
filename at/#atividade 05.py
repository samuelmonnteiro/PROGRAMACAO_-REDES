#atividade 05

# Entrada de dados
# os valores para o usuário
primeiro_termo = int(input("Digite o primeiro termo da PG: "))
razao = float(input("Digite a razão da PG: "))
quantidade = int(input("Digite quantos números quer ver: "))

# números da PG
print("\nNúmeros da PG:")
numero_atual = primeiro_termo
soma = 0

for i in range(quantidade):
    print(f"Número {i+1}: {numero_atual}")
    soma = soma + numero_atual
    numero_atual = numero_atual * razao

# Mostra a soma
print(f"\nA soma dos números é: {soma}")

# tipo de PG é
if razao == 1:
    print("Esta PG é constante")
elif razao > 1:
    print("Esta PG é crescente")
elif razao < 0:
    print("Esta PG é oscilante")
else:
    print("Esta PG é decrescente")

# número específico
posicao = int(input("\nQual posição você quer calcular? "))
resultado = primeiro_termo * (razao ** (posicao - 1))
print(f"O número na posição {posicao} é: {resultado}")