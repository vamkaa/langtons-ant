# Langton's Ant Simulator

Visual simulation of Langton's ant made with Python and Pygame.

Features:
- Custom rule input WITH R & L, default being RL
- 3 colormodes (grayscale, rainbow and random)
- Adjustable speed
- Press SPACE to make ONE step
- Press ENTER to run/pause
- Press arrow keys up / down to speed and slow it down

Try at least: 

RRLLLRLLLRRR Triangle thingy

LLRR Symmetrical (RRLL too)

RLRL sykkyrähighway

Default

# setup #

Clone the repository in powershell with:
- "git clone https://github.com/vamkaa/langtons-ant.git"

- cd langtons-ant

- create virtual environment with "python -m venv .venv"

- activate .venv with ".venv\Scripts\Activate.ps1"

- install dependencies (pygame) with "pip install -r requirements.txt"

- run the program with "python src/main.py"

# how to use #

after "python src/main.py", the terminal will ask for a string imput consisting of "L" and "R". Pressing enter wihtout typing any Ls or Rs will choosethe default "RL". 

then you will choose the color mode. Press enter to randomly pick one of the three options or type your preferred option in the terminal.

then use spacebar for single steps, enter for run/pause and up and down arrow keys for speeding up or slowing down. 

# hot tip, you can change window size and cell size to your liking from the config.py file. Enjoy.