#atidave 03
# Entrada de dados da questão 03
n = int(input('Digite um número: '))
if n <= 0:
    print('Informe um número inteiro maior que o numero  0!')
    exit()

# Encontra os fatores primos
fatores = []
numero = n
divisor = 2

while numero > 1:
    if numero % divisor == 0:
        fatores.append(divisor)
        numero //= divisor
    else:
        divisor += 1

# Verifica se tem exatamente 2 fatores primos
if len(fatores) == 2:
    print(f'{n} = {fatores[0]} × {fatores[1]}')
else:
    print(f'{n} não é um produto de dois números primos')