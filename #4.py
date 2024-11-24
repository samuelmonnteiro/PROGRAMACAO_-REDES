#4
# sistema com o número de dias em cada mês
dias_por_mes = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

# Entrada de dados do usuário
dia_inicial = int(input('Informe o dia inicial: '))
mes_inicial = int(input('Informe o mês inicial: '))
dia_final = int(input('Informe o dia final: '))
mes_final = int(input('Informe o mês final: '))

# Validação das entradas
if not (1 <= mes_inicial <= 12 and 1 <= mes_final <= 12):
    print("Mês inválido! Digite um mês entre 1 e 12.")
elif not (1 <= dia_inicial <= dias_por_mes[mes_inicial] and 1 <= dia_final <= dias_por_mes[mes_final]):
    print("Dia inválido para o mês informado!")
else:
    if mes_inicial == mes_final:
        diferenca_dias = dia_final - dia_inicial
    else:
        # Dias restantes no mês inicial
        diferenca_dias = dias_por_mes[mes_inicial] - dia_inicial
        
        # Adiciona os dias dos meses intermediários
        for mes in range(mes_inicial + 1, mes_final):
            diferenca_dias += dias_por_mes[mes]
            
        # Adiciona os dias do mês final
        diferenca_dias += dia_final
    
    print(f'Entre as datas informadas passaram-se {diferenca_dias} dia(s).')