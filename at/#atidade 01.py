#atividade
# Entrada de dados

def calcular_decaimento():
    # Solicita a massa inicial
    massa_inicial = int(input("Digite a massa inicial em gramas: "))
    
    massa_atual = massa_inicial
    tempo_total = 0
    
    # Calcula o decaimento até massa ser menor que 0.5
    while massa_atual >= 0.5:
        massa_atual /= 2  # Perde metade da massa
        tempo_total += 50  # Adiciona 50 segundos
    
    # coloca o total em segundos para horas, minutos e segundos
    horas = tempo_total // 3600
    minutos = (tempo_total % 3600) // 60
    segundos = tempo_total % 60
    
    # colocao no formato HH:MM:SS
    tempo_formatado = f"{int(horas):02d}:{int(minutos):02d}:{int(segundos):02d}"
    
    # resultados
    print(f"\nMassa Inicial: {massa_inicial} gramas")
    print(f"Massa Final: {massa_atual} gramas")
    print(f"Tempo de Decaimento: {tempo_formatado}")

# Executa o programa
calcular_decaimento()