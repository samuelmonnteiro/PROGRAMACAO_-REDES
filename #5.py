#5
# Entrada de dados do usuário
hr_chegada = int(input('Informe a hora da chegada (0 a 23): '))
min_chegada = int(input('Informe os minutos da chegada (0 a 59): '))
tot_min_chegada = (hr_chegada * 60) + min_chegada

hr_saida = int(input('Informe a hora da saída (0 a 23): '))
min_saida = int(input('Informe os minutos da saída (0 a 59): '))
tot_min_saida = (hr_saida * 60) + min_saida

# Ajuste para casos em que a saída é no dia seguinte
if tot_min_saida < tot_min_chegada:
    tot_min_saida += 24 * 60

# Cálculo do total de permanência em minutos
total_permanencia = tot_min_saida - tot_min_chegada

# Exibindo tempo de permanência
print(f'Você permaneceu em nosso estacionamento por {total_permanencia} minuto(s).')

# Calculando o valor a ser cobrado
if total_permanencia <= 60:
    vr_cobrado = 8  # Até 1 hora
elif total_permanencia <= 120:
    vr_cobrado = 16  # Até 2 horas
elif total_permanencia <= 180:
    vr_cobrado = 21  # Até 3 horas (2 horas + 5 reais)
elif total_permanencia <= 240:
    vr_cobrado = 26  # Até 4 horas (3 horas + 5 reais)
elif total_permanencia <= 720:
    vr_base = 26  # Valor das primeiras 4 horas
    min_extra = total_permanencia - 240  # Minutos além de 4 horas
    hr_extra = min_extra // 60  # Horas extras completas
    if min_extra % 60 > 0:  # Verifica se há fração de hora
        hr_extra += 1  # Adiciona uma hora adicional para fração
    vr_cobrado = vr_base + (hr_extra * 3)  # Soma 3 reais por hora ou fração extra
else:
    vr_cobrado = 30  # Mais de 12 horas

# Exibindo o valor a ser pago
print(f'Valor a ser pago: R$ {vr_cobrado:.2f}')
