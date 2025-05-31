import time
import pydirectinput


# Move a larva na direção indicada / Move the larva in the given direction
def move_steps(steps, direction):
    for _ in range(steps):
        pydirectinput.press(direction)
        time.sleep(0.1) 

# Executa os comandos da fase / Runs the stage commands
def run_stage(stage):
    for steps, direction in stage:
        move_steps(steps, direction)

# Troca para a próxima fase / Switches to the next stage
def next_stage():
    time.sleep(5)
    pydirectinput.press("right")
    pydirectinput.press("x")
    time.sleep(5)