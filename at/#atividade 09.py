#atividade 09
#entrada de dados 

# as sequências
sequencia1 = input("Digite a primeira sequência (só 0 e 1): ")
sequencia2 = input("Digite a segunda sequência (só 0 e 1): ")

# Verifica tamanho
if len(sequencia1) != len(sequencia2):
    print("ERRO: As sequências precisam ter o mesmo tamanho!")
else:
    # as respostas
    resultado_and = ""
    resultado_or = ""
    resultado_xor = ""
    
    # Faz cada operação
    for posicao in range(len(sequencia1)):
        # Pega os dígitos da posição atual
        digito1 = sequencia1[posicao]
        digito2 = sequencia2[posicao]
        
        # Operação AND
        if digito1 == "1" and digito2 == "1":
            resultado_and = resultado_and + "1"
        else:
            resultado_and = resultado_and + "0"
        
        # Operação OR
        if digito1 == "1" or digito2 == "1":
            resultado_or = resultado_or + "1"
        else:
            resultado_or = resultado_or + "0"
        
        # Operação XOR
        if digito1 != digito2:
            resultado_xor = resultado_xor + "1"
        else:
            resultado_xor = resultado_xor + "0"
    
    # Mostra os resultados
    print("\nResultados:")
    print("Sequência 1:", sequencia1)
    print("Sequência 2:", sequencia2)
    print("AND:", resultado_and)
    print("OR:", resultado_or)
    print("XOR:", resultado_xor)