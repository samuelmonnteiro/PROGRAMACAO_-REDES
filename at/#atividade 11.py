#atividade 11
#entrada de dados


# o alfabeto
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Solicitando o texto e a chave do usuário
texto = input('Digite o texto em maiúsculas: ')
chave = int(input('Digite a chave (número inteiro): '))

# Criptografando o texto
texto_cifrado = ''
for letra in texto:
    if letra in alfabeto:
        posicao = alfabeto.find(letra)  # Encontra a posição da letra
        nova_posicao = (posicao + chave) % 26  # Nova posição com a chave
        texto_cifrado += alfabeto[nova_posicao]
    else:
        texto_cifrado += letra 

# Descriptografando o texto
texto_decifrado = ''
for letra in texto_cifrado:
    if letra in alfabeto:
        posicao = alfabeto.find(letra)  
        nova_posicao = (posicao - chave) % 26  
        texto_decifrado += alfabeto[nova_posicao]
    else:
        texto_decifrado += letra  

# Exibindo os resultados
print('\nTexto original:', texto)
print('Texto cifrado:', texto_cifrado)
print('Texto decifrado:', texto_decifrado)
