#atividade 08 
#entrada de dados
numero = int(input("Digite um número: "))

# número
n = numero

#  dígitos
digitos = 0
while n > 0:
    digitos = digitos + 1
    n = n // 10

# para somar
n = numero
soma = 0

# Soma cada dígito elevado à potência
while n > 0:
    # o último dígito
    ultimo = n % 10
    
    # Eleva à potência e soma
    potencia = ultimo ** digitos
    soma = soma + potencia
    
    # Remove o último dígito
    n = n // 10

# o resultado
print(f"Número digitado: {numero}")
print(f"Soma calculada: {soma}")

if numero == soma:
    print("É número de Armstrong!")
else:
    print("Não é número de Armstrong!")