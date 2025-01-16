#atividade 04 

def calcular_soma_dos_digitos(numero, potencia):
    """Função que soma as potências dos dígitos de um número."""
    soma = 0
    for digito in str(numero):
        soma += int(digito) ** potencia
    return soma

# Procura números que obedecem à regra
for numero in range(2, 1000000):  
    if numero % 2 == 0 or numero % 5 == 0:  
        soma = calcular_soma_dos_digitos(numero, 5)  
        if soma == numero:  
            print(f"Achei: {numero}")  
            print(f"Soma: {soma}") 

