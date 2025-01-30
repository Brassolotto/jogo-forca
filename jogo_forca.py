import random

def escolher_palavra():
    palavras = ['PYTHON', 'PROGRAMACAO', 'COMPUTADOR', 'DESENVOLVIMENTO', 'TECNOLOGIA']
    return random.choice(palavras)

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
    palavra = escolher_palavra()
    palavra_oculta = ['_' for letra in palavra]  # Cria lista com underlines
    letras_erradas = []
    erros = 0
    
    print("Bem-vindo ao Jogo da Forca!")
    
    while True:
        print(mostrar_forca(erros))
        print(' '.join(palavra_oculta))  # Mostra a palavra com espaços
        print(f"\nLetras erradas: {' '.join(letras_erradas)}")
        
        if erros == 6:  # Perdeu o jogo
            print(f"\nVocê perdeu! A palavra era: {palavra}")
            break
            
        if '_' not in palavra_oculta:  # Ganhou o jogo
            print("\nParabéns! Você venceu!")
            break
            
        tentativa = input("\nDigite uma letra: ").upper()
        
        if tentativa in palavra_oculta or tentativa in letras_erradas:
            print("\nVocê já tentou essa letra!")
            continue
            
        if tentativa in palavra:
            for i in range(len(palavra)):
                if palavra[i] == tentativa:
                    palavra_oculta[i] = tentativa
        else:
            letras_erradas.append(tentativa)
            erros += 1
            print("\nLetra errada!")

if __name__ == "__main__":
    main()

    
