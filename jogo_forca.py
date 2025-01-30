import random

def escolher_palavra():
    categorias = {
        'ANIMAIS': ['CACHORRO', 'GATO', 'ELEFANTE', 'GIRAFA', 'LEAO'],
        'FRUTAS': ['BANANA', 'MAÇA', 'LARANJA', 'UVA', 'MORANGO'],
        'PAÍSES': ['BRASIL', 'PORTUGAL', 'ESPANHA', 'ITALIA', 'FRANÇA'],
        'PROFISSÕES': ['PROFESSOR', 'MEDICO', 'ENGENHEIRO', 'ADVOGADO', 'PROGRAMADOR']
    }

    print("\nEscolha uma categoria:")
    for i, categoria in enumerate(categorias.keys(), 1):
        print(f"{i}. {categoria}")

    while True:
        try:
            escolha = int(input("\nDigite o número da categoria: "))
            if 1 <= escolha <= len(categorias):
                categoria_escolhida = list(categorias.keys())[escolha - 1]
                palavra = random.choice(categorias[categoria_escolhida])
                return palavra, categoria_escolhida
            else:
                print("Número inválido! Tente novamente.")
        except ValueError:
            print("Por favor, digite um número!")

def validar_entrada(tentativa, letras_usadas):
    if not tentativa.isalpha():
        return False, "Por favor, digite apenas letras!"
    if len(tentativa) != 1:
        return False, "Digite apenas uma letra por vez!"
    if tentativa in letras_usadas:
        return False, "Você já tentou essa letra!"
    return True, ""


def mostrar_forca(erros):
    estagios = [  # estágios do desenho da forca
        """
           +---+
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    return estagios[erros]

def main():
    while True:

        palavra, categoria = escolher_palavra()
        palavra_oculta = ['_' for letra in palavra]  # Cria lista com underlines
        letras_erradas = []
        letras_usadas = []
        erros = 0
        
        print("Bem-vindo ao Jogo da Forca!")
    
        while True:
            print(mostrar_forca(erros))
            print(f"\nCategoria: {categoria}")
            print(f"Palavra: {' '.join(palavra_oculta)}")
            print(f"Letras erradas: {' '.join(letras_erradas)}")
            print(f"Tentativas restantes: {6 - erros}")
            
            if erros == 6:  # Perdeu o jogo
                print(f"\nVocê perdeu! A palavra era: {palavra}")
                break
                
            if '_' not in palavra_oculta:  # Ganhou o jogo
                print("\nParabéns! Você venceu!")
                break
                
            tentativa = input("\nDigite uma letra: ").upper()
            valida, mensagem = validar_entrada(tentativa, letras_usadas)

            if not valida:
                print(mensagem)
                continue

            letras_usadas.append(tentativa)
                
            if tentativa in palavra:
                for i in range(len(palavra)):
                    if palavra[i] == tentativa:
                        palavra_oculta[i] = tentativa
                print("\nLetra correta!")
            else:
                letras_erradas.append(tentativa)
                erros += 1
                print("\nLetra errada!")

        jogar_novamente = input("\nQuer jogar novamente? (S/N): ").upper()
        if jogar_novamente != 'S':
            print("\nObrigado por jogar!")
            break

if __name__ == "__main__":
    main()

    
