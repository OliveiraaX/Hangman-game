import requests
import re
import unicodedata

url = 'https://www.palavrasque.com/palavra-aleatoria.php'
req = requests.get(url)

if req.status_code == 200:
    content_type = req.headers.get('content-type')
    encoding = 'utf-8'
    if content_type and 'charset=' in content_type:
        encoding = content_type.split('charset=')[1]

    html_content = req.content.decode(encoding, errors='ignore')
    pattern = r'<b>(.*?)</b>'
    matches = re.findall(pattern, html_content)

    for match in matches:
        print('Palavra aleatória escolhida com sucesso:')
else:
    print("Erro ao escolher palavra")

# Definindo a variável palavra 
palavra = match.lower()

# Inicialização de variáveis
tentativas = 6  # Número máximo de tentativas
letras_corretas = []
letras_erradas = []
palavra_adivinhada = ["_"] * len(palavra)

def hangman():
    if tentativas == 6:
        print('''             |--------|
	              |
	              |
	       	      |
                      |
                      |
                      -''')
    if tentativas == 5:
        print('''             |--------|
             O        |
                      |
                      |
                      |
                      |
                      -''')
    if tentativas == 4:
        print('''             |--------|
             O        |
             |        |
                      |
                      |
                      |
                      -''')
    if tentativas == 3:
        print('''             |--------|
             O        |
            /|        |
                      |
                      |
                      |
                      -''')
    if tentativas == 2:
        print('''             |--------|
             O        |
            /|\       |
                      |
                      |
                      |
                      -''')
    if tentativas == 1:
        print('''             |--------|
             O        |
            /|\       |
            /         |
                      |
                      |
                      -''')
    if tentativas == 0:
        print('''             |--------|
             O        |
            /|\       |
            / \       |
                      |
                      |
                      -''')
# Função para exibir o status do jogo
def exibir_jogo():
    hangman()
    print("\nPalavra: " + " ".join(palavra_adivinhada))
    print("\nTentativas Restantes: " + str(tentativas))
    print("\nLetras Erradas: " + ", ".join(letras_erradas))

# Função para remover acentos de uma letra
def remover_acentos(letra):
    return ''.join(c for c in unicodedata.normalize('NFD', letra) if unicodedata.category(c) != 'Mn')

# Loop principal do jogo
while tentativas > 0 and "_" in palavra_adivinhada:
    exibir_jogo()

    # Obtenha a suposição do jogador
    palpite = input("\nDigite uma letra: ").lower()

    # Remova acentos do palpite
    palpite = remover_acentos(palpite)

    # Verifique se o palpite é válido
    if len(palpite) != 1 or not palpite.isalpha():
        print("Por favor, insira uma única letra válida.")
        continue

    # Remova acentos das letras da palavra
    palavra_sem_acentos = ''.join(remover_acentos(letra) for letra in palavra)

    # Verifique se o palpite já foi feito
    if palpite in letras_corretas or palpite in letras_erradas:
        print("Você já tentou esta letra antes.")
        continue

    # Verifique se o palpite está na palavra
    if palpite in palavra_sem_acentos:
        letras_corretas.append(palpite)
        for i in range(len(palavra)):
            if remover_acentos(palavra[i]) == palpite:
                palavra_adivinhada[i] = palavra[i]
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
