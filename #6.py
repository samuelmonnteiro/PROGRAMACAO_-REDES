#6 
from datetime import datetime
from dateutil.relativedelta import relativedelta

def calcular_data_aposentadoria(sexo, data_nascimento, data_inicio_contribuicao):
    # Converter as datas de entrada para objetos datetime
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    data_inicio = datetime.strptime(data_inicio_contribuicao, "%d/%m/%Y")

    # Determinar requisitos de idade e tempo de contribuição
    if sexo.lower() == 'masculino':
        idade_minima = 65
        tempo_contribuicao_minimo = 35
    elif sexo.lower() == 'feminino':
        idade_minima = 62
        tempo_contribuicao_minimo = 30
    else:
        return "Sexo inválido. Use 'masculino' ou 'feminino'."

    # Calcular data de aposentadoria baseada na idade mínima
    data_aposentadoria_idade = data_nascimento + relativedelta(years=idade_minima)

    # Calcular data de aposentadoria baseada no tempo de contribuição
    data_aposentadoria_tempo = data_inicio + relativedelta(years=tempo_contribuicao_minimo)

    # Calcular data mínima de contribuição (15 anos de contribuição)
    tempo_min_contribuicao = 15
    data_min_contribuicao = data_inicio + relativedelta(years=tempo_min_contribuicao)

    # Garantir que a aposentadoria por idade respeite os 15 anos mínimos de contribuição
    if data_aposentadoria_idade < data_min_contribuicao:
        data_aposentadoria_idade = data_min_contribuicao

    # Determinar a data final de aposentadoria considerando o maior requisito
    data_aposentadoria = max(data_aposentadoria_idade, data_aposentadoria_tempo)

    # Retornar a data formatada
    return data_aposentadoria.strftime("%d/%m/%Y")

# Entrada do usuário
sexo = input('Sexo (Feminino ou Masculino): ')
data_nascimento = input('Qual sua data de nascimento (dd/mm/aaaa): ')
data_inicio_de_contribuicao = input('Data de início de contribuição (dd/mm/aaaa): ')

# Calcular a data de aposentadoria
resultado = calcular_data_aposentadoria(sexo, data_nascimento, data_inicio_de_contribuicao)

# Exibir o resultado
print(f'A data prevista mais próxima será: {resultado}')
