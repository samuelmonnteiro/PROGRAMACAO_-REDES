#questao 06 
#entrada de dados 

# Entrada dos valores
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
quantidade = int(input("Digite quantos números quer ver: "))

# os números da PA
print("\nNúmeros da PA:")
numero_atual = primeiro_termo
soma = 0

for i in range(quantidade):
    print(f"Número {i+1}: {numero_atual}")
    soma = soma + numero_atual
    numero_atual = numero_atual + razao  

# a soma
print(f"\nA soma dos números é: {soma}")

# tipo de PA
if razao == 0:
    print("Esta PA é constante")
elif razao > 0:
    print("Esta PA é crescente")
else:
    print("Esta PA é decrescente")

# Calcula número específico
posicao = int(input("\nQual posição você quer calcular? "))
resultado = primeiro_termo + (posicao - 1) * razao 
print(f"O número na posição {posicao} é: {resultado}")