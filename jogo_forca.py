import random

def escolher_palavra():
    palavras = ['PYTHON', 'PROGRAMACAO', 'COMPUTADOR', 'DESENVOLVIMENTO', 'TECNOLOGIA']

    return random.choice(palavras)

def mostrar_forca(erros):
    estagios = [
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


    
