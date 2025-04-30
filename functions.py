import time
import pydirectinput


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