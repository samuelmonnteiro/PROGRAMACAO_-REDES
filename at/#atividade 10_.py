#atividade 10_
#ENTRADA DE DADOS 

def kaprekar(numero):
    # que o número tenha 4 dígitos
    numero = str(numero)
    while len(numero) < 4:
        numero = '0' + numero
    
    # Cria o menor e maior número a partir dos dígitos
    menor = int("".join(sorted(numero)))
    maior = int("".join(sorted(numero, reverse=True)))
    
    # Retorna a diferença entre o maior e o menor
    return maior - menor

# um número do usuário
enquanto_valido = True
while enquanto_valido:
    entrada = input("Digite um número de até 4 dígitos: ")
    
    if entrada.isdigit() and 0 < int(entrada) < 10000:
        numero = int(entrada)
        
        # Ver se todos os dígitos são iguais
        if len(set(str(numero))) == 1:
            print("Número inválido! Digite um número com pelo menos dois dígitos diferentes.")
        else:
            # Processa o número pelo método de Kaprekar
            iteracoes = 0
            print("Iterações:")
            while numero != 6174:
                novo_numero = kaprekar(numero)
                numero_str = str(numero)
                while len(numero_str) < 4:
                    numero_str = '0' + numero_str
                novo_numero_str = str(novo_numero)
                while len(novo_numero_str) < 4:
                    novo_numero_str = '0' + novo_numero_str
                print(f"{numero_str} -> {novo_numero_str}")
                numero = novo_numero
                iteracoes += 1
            print(f"\nNúmero total de iterações: {iteracoes}")
            enquanto_valido = False
    else:
        print("Entrada inválida! Digite um número entre 1 e 9999.")
        
