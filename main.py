import pyautogui as pg
import pydirectinput 
import time

# Função que determina a quantidade de passos/direção 
def quantidade_passos(passos, sentido):
    for _ in range(passos):
        pydirectinput.press(sentido)
        time.sleep(0.1) 

# Função para executar cada fase
def executar_fase(fase):
    for passos, direcao in fase:
        quantidade_passos(passos, direcao)

# Função para mudar de fase
def troca_fase():
    time.sleep(5)
    pydirectinput.press("right")
    pydirectinput.press("x")
    time.sleep(5)

# Entra no chrome e entra no woodworm
pg.press("win")
time.sleep(2)
pg.write("chrome")
pg.press("enter")
time.sleep(2)
pg.write("https://spratt.itch.io/woodworm")
pg.press("enter")
time.sleep(5)

# Posição do click: x=950, y=450
pg.click(x=950, y=450)
time.sleep(8)

# Inicia o jogo selecionando a primeira fase
pydirectinput.press("x")
time.sleep(1)
pydirectinput.press("x")
time.sleep(1)
pydirectinput.press("x")
time.sleep(8)

# Primira fase
fase1 = [
    (3, "right"),
    (1, "up"),
    (2, "left"),
    (4, "up"),
    (1, "right"),
    (1, "up"),
    (4, "right"),
    (1, "down"),
    (1, "right"),
    (3, "down"),
    (2, "left"),
    (1, "down"),
    (1, "right"),
]

executar_fase(fase1)
troca_fase()

fase2 = [
    (1, "right"),
    (6, "up"),
    (2, "right"),
    (2, "down"),
    (1, "right"),
    (1, "up"),
    (1, "right"),
    (1, "up"),
    (2, "right"),
    (1, "down"),
    (1, "right"),
    (3, "down"),
    (2, "left"),
    (1, "down"),
    (1, "right"),
    (1, "down"),
    (1, "left"),
    (2, "left"),
    (1, "up"),
    (1, "left"),
    (1, "down"),
    (1, "left"),
]

executar_fase(fase2)