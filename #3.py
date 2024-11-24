#3
# Entrada de dados
hora_partida = int(input("Digite a hora de partida (0-23): "))
minuto_partida = int(input("Digite o minuto de partida (0-59): "))
hora_chegada = int(input("Digite a hora de chegada (0-23): "))
minuto_chegada = int(input("Digite o minuto de chegada (0-59): "))
tempo_parado = int(input("Digite o tempo parado em segundos: "))
litros_gastos = float(input("Digite a quantidade de litros gastos: "))
preco_litro = float(input("Digite o preço do litro de combustível (R$): "))
distancia = float(input("Digite a distância percorrida (Km): "))

# Validação dos dados
if not (0 <= hora_partida <= 23) or not (0 <= minuto_partida <= 59):
    print("Hora ou minuto de partida inválidos!")
elif not (0 <= hora_chegada <= 23) or not (0 <= minuto_chegada <= 59):
    print("Hora ou minuto de chegada inválidos!")
else:
    # Cálculo do tempo total em minutos
    tempo_partida = hora_partida * 60 + minuto_partida
    tempo_chegada = hora_chegada * 60 + minuto_chegada

    if tempo_chegada < tempo_partida:
        tempo_chegada += 24 * 60  # Adiciona 24 horas se a viagem passou para o dia seguinte

    tempo_total = tempo_chegada - tempo_partida
    tempo_movimento = tempo_total - (tempo_parado / 60)

    # Cálculos de desempenho
    if tempo_movimento > 0 and litros_gastos > 0 and distancia > 0:
        # Velocidade média em km/h
        velocidade_media = (distancia / tempo_movimento) * 60
        
        # Consumo médio em km/l
        consumo_medio = distancia / litros_gastos
        
        # Custo total do combustível
        custo_total = litros_gastos * preco_litro
        
        # Exibição dos resultados
        print("\nRelatório da Viagem:")
        print(f"Tempo total de viagem: {tempo_total} minutos")
        print(f"Tempo em movimento: {tempo_movimento:.2f} minutos")
        print(f"Velocidade média: {velocidade_media:.2f} km/h")
        print(f"Consumo médio: {consumo_medio:.2f} km/l")
        print(f"Custo total com combustível: R$ {custo_total:.2f}")
    else:
        print("Erro: Valores inválidos inseridos!")
