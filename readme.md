# Woodworm Bot
Um projeto simples usando Python para zerar o jogo Woodworm automaticamente 

## Sobre o jogo
Woodworm é um jogo simples presente no navegador e possui poucos comandos, onde você controla um cupim que precisa esculpir figuras na madeira.

## O que o bot faz?
- Entra no chrome.
- Acessa o site do jogo.
- Inicia o jogo. 
- Percorre todas as fases até zerar.

## Tecnologias utilizadas
- Python
- PyAutogui - Para acessar o site do jogo.
- PydirectInput - Para simular as interações a partir das setas.
- Time - Usada para pausas e temporizações.

## Como rodar:
1° Instale as dependências:
```bash
pip install pyautogui pydirectinput
```

2° Execute o script: 
```bash
python main.py
```

3° Deixe o jogo aberto e com foco.

## Objetivo
Esse projeto foi feito apenas por diversão e aprendizado com automação.