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
run_stage(fase1)
next_stage()

# Segunda fase
run_stage(fase2)
next_stage()

# Terceira fase
run_stage(fase3)
next_stage()

# Quarta fase
run_stage(fase4)
next_stage()

# Quinta fase
run_stage(fase5)
next_stage()

# Sexta fase
run_stage(fase6)
next_stage()

# Setima fase 
run_stage(fase7)
next_stage()

# Oitava fase
run_stage(fase8)