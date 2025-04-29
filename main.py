import pyautogui as pg
import pydirectinput 
import time

# Função que determina a quantidade de passos/direção 
def move_steps(steps, direction):
    for _ in range(steps):
        pydirectinput.press(direction)
        time.sleep(0.1) 

# Função para executar cada fase
def run_stage(stage):
    for steps, direction in stage:
        move_steps(steps, direction)

# Função para mudar de fase
def next_stage():
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

run_stage(fase1)
next_stage()

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

run_stage(fase2)