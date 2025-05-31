import pyautogui as pg
import pydirectinput 
import time
from functions import run_stage, move_steps, next_stage
from levels import * 
import subprocess

# Abre o Chrome e acessa o jogo Woodworm / Open Chrome and access the Woodworm game
subprocess.Popen([
    "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "--incognito",
    "https://spratt.itch.io/woodworm"
])

# Inicia o jogo / Starts the game
time.sleep(5)
pg.click(x=950, y=450)
time.sleep(8)

# Entra no menu de fases e seleciona a primeira / Enters the level menu and selects the first one
pydirectinput.press("x")
time.sleep(1)
pydirectinput.press("x")
time.sleep(1)
pydirectinput.press("x")
time.sleep(8)

# Primeira fase / First level
run_stage(level_1)
next_stage()

# Segunda fase / Second level
run_stage(level_2)
next_stage()

# Terceira fase / Third level
run_stage(level_3)
next_stage()

# Quarta fase / Fourth level
run_stage(level_4)
next_stage()

# Quinta fase / Fifth level
run_stage(level_5)
next_stage()

# Sexta fase / Sixth level
run_stage(level_6)
next_stage()

# Sétima fase / Seventh level
run_stage(level_7)
next_stage()

# Oitava fase / Eighth level
run_stage(level_8)
next_stage()

# Nona fase / Ninth level
run_stage(level_9)
next_stage()

# Décima fase / Tenth level
run_stage(level_10)
next_stage()

# Décima primeira fase / Eleventh level
run_stage(level_11)
next_stage()

# Décima segunda fase / Twelfth level
run_stage(level_12)
next_stage()

# Décima terceira fase / Thirteenth level
run_stage(level_13)
next_stage()

# Décima quarta fase / Fourteenth level
run_stage(level_14)
next_stage()

# Décima quinta fase / Fifteenth level
run_stage(level_15)
next_stage()

# Décima sexta fase / Sixteenth level
run_stage(level_16)
next_stage()

# Décima sétima fase / Seventeenth level
run_stage(level_17)