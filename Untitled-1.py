from brasileirao_serie_a import clubes

# Convertendo a string de clubes em uma lista de listas
lstclubes = clubes.split('\n')
lstclubes = [linha.split(';') for linha in clubes.split('\n')]

def obter_classificacao(ano):
    #os dados pelo ano informado
    dados_ano = [clube for clube in lstclubes if int(clube[1]) == ano]
    
    # Calcula os pontos
    classificacao = []
    for clube in dados_ano:
        vitorias = int(clube[2])
        empates = int(clube[3])
        derrotas = int(clube[4])
        gols_pro = int(clube[5])
        gols_contra = int(clube[6])
        pontos = vitorias * 3 + empates
        saldo_gols = gols_pro - gols_contra
        aproveitamento = pontos / (vitorias + empates + derrotas) * 100
        classificacao.append([clube[0], pontos, vitorias, empates, derrotas, gols_pro, gols_contra, saldo_gols, aproveitamento])
    
    # Ordena a classificação por pontos e saldo de gols
    classificacao.sort(key=lambda x: (x[1], x[7]), reverse=True)
     
    # Exibe a classificação
    for i, clube in enumerate(classificacao, 1):
        print(f"{i:02d}. {clube[0]} {clube[1]} {clube[2]} {clube[3]} {clube[4]} {clube[5]} {clube[6]} {clube[7]} {clube[8]:.2f}%")

if __name__ == "__main__":
    ano = int(input("Informe o ano da competição (2019-2024): "))
    if 2019 <= ano <= 2024:
        obter_classificacao(ano)
    else:
        print("Ano inválido. Por favor, informe um ano entre 2019 e 2024.")
