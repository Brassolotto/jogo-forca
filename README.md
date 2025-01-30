# Jogo da Forca em Python

## 📝 Descrição
Uma implementação do clássico jogo da forca com interface via terminal, múltiplas categorias de palavras e arte ASCII. O jogador deve adivinhar a palavra oculta antes que o boneco seja completamente desenhado.

## 🎮 Funcionalidades
- Múltiplas categorias de palavras
- Arte ASCII da forca
- Validação completa de entradas
- Contagem de tentativas
- Sistema de dicas (categoria)
- Opção de jogar novamente
- Interface amigável via terminal

## 🎯 Como Jogar
1. Escolha uma categoria
2. Tente adivinhar a palavra letra por letra
3. Você tem 6 tentativas antes que o boneco seja completado
4. Letras corretas são reveladas na palavra
5. Letras erradas são mostradas separadamente

## 📋 Regras
- Apenas uma letra por vez
- Não são permitidos números ou caracteres especiais
- Letras repetidas não contam como tentativa
- 6 erros completam o boneco e encerram o jogo

## 🎨 Interface do Jogo
```
   +---+
   |   |
   O   |    Categoria: ANIMAIS
  /|\  |    Palavra: C _ C H _ R R _
  / \  |    Letras erradas: B, F, I, J
       |    Tentativas restantes: 2
=========
```

## 🔧 Como executar
1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/jogo-forca.git
```

2. Navegue até o diretório do projeto:
```bash
cd jogo-forca
```

3. Execute o jogo:
```bash
python jogo_forca.py
```

## 📋 Pré-requisitos
- Python 3.6 ou superior
- Não requer bibliotecas externas

## ⚙️ Estrutura do Código
```
jogo_forca.py
├── Função escolher_palavra()
├── Função mostrar_forca()
├── Função validar_entrada()
└── Função main()
```

## 📚 Categorias Disponíveis
- Animais
- Frutas
- Países
- Profissões

## 🤝 Contribuindo
Contribuições são bem-vindas! Para contribuir:
1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adicionando nova feature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

## ✨ Possíveis Melhorias Futuras
- [ ] Adicionar mais categorias
- [ ] Sistema de pontuação
- [ ] Níveis de dificuldade
- [ ] Modo multiplayer
- [ ] Interface gráfica
- [ ] Banco de dados de palavras
- [ ] Sistema de rankings

## 📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor
Seu Nome
- GitHub: [@seu-usuario](https://github.com/Brassolotto)
- LinkedIn: [@seu-linkedin](https://linkedin.com/in/ricardo-brassolotto)

---
⌨️ com ❤️ por [Rick Brassolotto] 😊