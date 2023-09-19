import random

# Lista de palavras para o jogo // Coloque suas palavras!
palavras = ["", "", "", "", "", "", '']


# Escolha aleatoriamente uma palavra da lista
palavra = random.choice(palavras)

# Inicialização de variáveis
tentativas = 6  # Número máximo de tentativas
letras_corretas = []
letras_erradas = []
palavra_adivinhada = ["_"] * len(palavra)

# Função para exibir o status do jogo
def exibir_jogo():
    print("\nPalavra: " + " ".join(palavra_adivinhada))
    print("\nTentativas Restantes: " + str(tentativas))
    print("\nLetras Erradas: " + ", ".join(letras_erradas))

# Loop principal do jogo
while tentativas > 0 and "_" in palavra_adivinhada:
    exibir_jogo()

    # Obtenha a suposição do jogador
    palpite = input("\nDigite uma letra: ").lower()

    # Verifique se o palpite é válido
    if len(palpite) != 1 or not palpite.isalpha():
        print("Por favor, insira uma única letra válida.")
        continue

    # Verifique se o palpite já foi feito
    if palpite in letras_corretas or palpite in letras_erradas:
        print("Você já tentou esta letra antes.")
        continue

    # Verifique se o palpite está na palavra
    if palpite in palavra:
        letras_corretas.append(palpite)
        for i in range(len(palavra)):
            if palavra[i] == palpite:
                palavra_adivinhada[i] = palpite
    else:
        letras_erradas.append(palpite)
        tentativas -= 1

# Exibir resultado final do jogo
exibir_jogo()

# Verifique se o jogador ganhou ou perdeu
if "_" not in palavra_adivinhada:
    print("\nParabéns! Você adivinhou a palavra: " + palavra)
else:
    print("\nVocê perdeu. A palavra era: " + palavra)
