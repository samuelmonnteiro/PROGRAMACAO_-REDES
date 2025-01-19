#questao 07
# entrada de dados 

# número para o usuário
numero = int(input("Digite um número: "))

# número 1
contador = 1
soma = 0

# somando os números até achar ou passar
while soma < numero:
    soma = soma + contador
    
    # Se achou o número
    if soma == numero:
        print(f"O número {numero} é triangular!")
        print(f"É a soma: ", end="")
        for i in range(1, contador + 1):
            if i < contador:
                print(i, end=" + ")
            else:
                print(i)
        break
    
    # Se passou do número
    if soma > numero:
        print(f"O número {numero} não é triangular!")
        break
        
    contador = contador + 1