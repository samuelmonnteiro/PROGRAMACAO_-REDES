#atidade 12
#ENTRADA DE DADOS


# palavra chave
PALAVRA_CHAVE = "futebol"

# variáveis
letras_corretas = ['_'] * len(PALAVRA_CHAVE) 
tentativas_erradas = 0
letras_erradas = []

print("Bem-vindo ao jogo da forca!")
print("A palavra tem", len(PALAVRA_CHAVE), "letras.")

# Loop principal do jogo
while tentativas_erradas < 6:
    print("\nPalavra:", " ".join(letras_corretas))
    print("Letras erradas:", ", ".join(letras_erradas))
    print("Tentativas restantes:", 6 - tentativas_erradas)
    
    letra = input("Digite uma letra: ").lower()  
    
    # Ver se a letra está na palavra
    if letra in PALAVRA_CHAVE:
        print(f"A letra '{letra}' está correta!")
        
        # Substitui pela letra correta
        for i in range(len(PALAVRA_CHAVE)):
            if PALAVRA_CHAVE[i] == letra:
                letras_corretas[i] = letra
    else:
        print(f"A letra '{letra}' não está na palavra.")
        letras_erradas.append(letra)  
        tentativas_erradas += 1  

    # Ver se o jogador já acertou todas as letras
    if '_' not in letras_corretas:
        print("\nParabéns! Você acertou a palavra:", PALAVRA_CHAVE)
        break
else:
    print("\nVocê perdeu! A palavra era:", PALAVRA_CHAVE)