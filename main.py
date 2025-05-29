import pyautogui as pg
import pydirectinput 
import time
from functions import run_stage, move_steps, next_stage
from levels import * 

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

# Primeira fase
run_stage(level_1)
next_stage()

# Segunda fase
run_stage(level_2)
next_stage()

# Terceira fase
run_stage(level_3)
next_stage()

# Quarta fase
run_stage(level_4)
next_stage()

# Quinta fase
run_stage(level_5)
next_stage()

# Sexta fase
run_stage(level_6)
next_stage()

# Setima fase 
run_stage(level_7)
next_stage()

# Oitava fase
run_stage(level_8)
next_stage()

# Nona fase
run_stage(level_9)
next_stage()

# Decima fase
run_stage(level_10)
next_stage()

# Decima primeira fase
run_stage(level_11)
next_stage()

# Decima segunda fase
run_stage(level_12)
next_stage()

# Decima terceira fase
run_stage(level_13)
next_stage()

# Decima quarta fase
run_stage(level_14)
next_stage()

# Decima quinta fase
run_stage(level_15)
next_stage()

# Decima sexta fase
run_stage(level_16)
next_stage()

# Decima setima fase
run_stage(level_17)