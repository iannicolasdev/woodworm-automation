# Woodworm Bot  
A simple Python project that automatically completes the game *Woodworm*.

## About the game  
Woodworm is a simple browser-based game with a few basic commands, where you control a termite that must carve shapes into wood.

## What does the bot do?  
- Opens Chrome.
- Navigates to the game's website.
- Starts the game.
- Automatically plays through all levels.

## Technologies used  
- Python – The core language of the project.
- PyAutoGUI – Used to start the game.
- PyDirectInput – Used to simulate keyboard arrow key inputs.
- Time – Used for delays and timing.  
- Subprocess – Used to open the game website in an incognito window.

## How to run:
1° Install the dependents
```bash
pip install pyautogui pydirectinput
```

2° Run the script: 
```bash
python main.py
```

3° Make sure the game is open and focused.

## Purpose
This project was created just for fun and to learn more about automation.